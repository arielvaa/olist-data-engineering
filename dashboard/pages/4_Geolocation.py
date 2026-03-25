import streamlit as st
import duckdb
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Geographic Intelligence", layout="wide")

@st.cache_data
def load_data():
    conn = duckdb.connect("../olist.db")
    return conn.execute("""
        SELECT 
            g.geolocation_lat as lat, 
            g.geolocation_lng as lon,
            COUNT(*) as density
        FROM customers c
        JOIN geolocation g ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
        GROUP BY 1, 2
        LIMIT 20000
    """).fetchdf()

df = load_data()

with st.sidebar:
    st.header("Kamus Istilah")
    with st.expander("Geospatial Analysis"):
        st.write("Analisis data yang memiliki komponen lokasi (koordinat). Berguna untuk menentukan letak gudang atau area promosi.")
    with st.expander("Hexagon Layer"):
        st.write("Metode pengelompokan titik data ke dalam bentuk segi enam. Semakin tinggi/merah hexagon, semakin padat pelanggan di area tersebut.")

st.title("Customer Geographic Distribution")
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=-15.78,
        longitude=-47.93,
        zoom=3,
        pitch=45,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=20000,
            elevation_scale=50,
            elevation_range=[0, 3000],
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=1000,
        ),
    ],
))

st.info("""
**Insight Lokasi:**
- Konsentrasi pelanggan tertinggi berada di wilayah **Tenggara Brasil** (Area Sao Paulo dan Rio de Janeiro).
- Semakin tinggi batang hexagon, semakin banyak jumlah pelanggan di koordinat tersebut.
""")