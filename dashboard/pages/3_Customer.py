import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(page_title="Customer Intelligence", layout="wide")

@st.cache_data
def load_data(query):
    conn = duckdb.connect("../olist.db")
    return conn.execute(query).fetchdf()

df = load_data("SELECT * FROM customer_mart")

with st.sidebar:
    st.header("Kamus Istilah")
    with st.expander("Customer Segmentation"):
        st.write("""
        Proses membagi pelanggan ke dalam kelompok berdasarkan perilaku belanja mereka (dalam hal ini berdasarkan total uang yang dihabiskan).
        """)
    with st.expander("Low, Medium, High, VIP"):
        st.write("""
        Pengelompokan (Binning) berdasarkan jumlah belanja:
        - **Low**: $0 - $100
        - **Medium**: $100 - $500
        - **High**: $500 - $1000
        - **VIP**: > $1000
        """)
    with st.expander("Customer Mart"):
        st.write("Tabel yang sudah digabungkan khusus untuk melihat profil tiap pelanggan unik (Total belanja, jumlah order, dll).")

st.title("Customer Intelligence")

df['segment'] = pd.cut(
    df['total_spent'],
    bins=[0, 100, 500, 1000, 100000], 
    labels=["Low", "Medium", "High", "VIP"]
)

st.subheader("Customer Distribution by Segment")
segment_counts = df['segment'].value_counts().reindex(["Low", "Medium", "High", "VIP"])
st.bar_chart(segment_counts)

top = df.sort_values("total_spent", ascending=False).iloc[0]

st.success(f"""
**Top Customer Insight**
- **Customer ID**: `{top['customer_id']}`
- **Total Spent**: ${top['total_spent']:,.0f}
- **Total Orders**: {top['total_orders']}
""")

st.subheader("Top 20 High-Value Customers")
st.dataframe(
    df.sort_values("total_spent", ascending=False)
    .head(20)
    .style.format({'total_spent': '${:,.2f}'})
)