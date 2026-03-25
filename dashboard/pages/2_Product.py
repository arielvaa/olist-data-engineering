import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(page_title="Product Intelligence", layout="wide")

@st.cache_data
def load_data(query):
    conn = duckdb.connect("../olist.db")
    return conn.execute(query).fetchdf()

df = load_data("""
SELECT * FROM product_mart
ORDER BY total_revenue DESC
""")

df['contribution_%'] = (df['total_revenue'] / df['total_revenue'].sum()) * 100

with st.sidebar:
    st.header("Kamus Istilah")
    with st.expander("Contribution %"):
        st.write("Persentase kontribusi pendapatan kategori tersebut terhadap total seluruh pendapatan.")
    with st.expander("Product Mart"):
        st.write("Tabel ringkasan (Data Mart) yang khusus berisi metrik performa produk seperti total terjual dan total revenue.")

st.title("Product Intelligence")

st.subheader("Top 10 Categories by Revenue")
st.bar_chart(df.head(10).set_index("category")["total_revenue"])

top_cat = df.iloc[0]
st.success(f"""
**Top Category: {top_cat['category']}**
- Revenue: **${top_cat['total_revenue']:,.0f}**
- Contribution: **{top_cat['contribution_%']:.2f}%**
""")

st.subheader("Full Product Data")
st.dataframe(df.style.format({
    'total_revenue': '${:,.2f}',
    'contribution_%': '{:.2f}%'
}))