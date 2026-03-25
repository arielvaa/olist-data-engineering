import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(page_title="Executive Overview", layout="wide")

@st.cache_data
def load_data(query):
    conn = duckdb.connect("../olist.db")
    return conn.execute(query).fetchdf()

df = load_data("SELECT * FROM sales_mart")
df['order_date'] = pd.to_datetime(df['order_date'])

with st.sidebar:
    st.header("Konfigurasi")
    min_date = df['order_date'].min().date()
    max_date = df['order_date'].max().date()
    start_date = st.date_input("Start Date", min_date)
    end_date = st.date_input("End Date", max_date)

    st.markdown("---")
    st.header("Kamus Istilah")
    with st.expander("Revenue"):
        st.write("Total nilai uang yang diterima dari penjualan barang.")
    with st.expander("AOV (Average Order Value)"):
        st.write("Rata-rata nilai transaksi per pesanan. Rumus: Total Revenue / Total Orders.")
    with st.expander("MoM Growth"):
        st.write("Persentase pertumbuhan pendapatan dibandingkan bulan sebelumnya.")
    with st.expander("Rolling Average"):
        st.write("Rata-rata bergerak 7 hari untuk melihat tren jangka panjang tanpa gangguan fluktuasi harian.")

mask = (df['order_date'].dt.date >= start_date) & (df['order_date'].dt.date <= end_date)
df_filtered = df.loc[mask].copy()

total_revenue = df_filtered['total_revenue'].sum()
total_orders = df_filtered['total_orders'].sum()
aov = total_revenue / total_orders if total_orders > 0 else 0

df_filtered['month_period'] = df_filtered['order_date'].dt.to_period('M')
monthly = df_filtered.groupby('month_period')['total_revenue'].sum().reset_index()

growth = 0
if len(monthly) > 1:
    current_month = monthly.iloc[-1, 1]
    prev_month = monthly.iloc[-2, 1]
    growth = ((current_month - prev_month) / prev_month) * 100

st.title("Executive Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Revenue", f"${total_revenue:,.0f}")
col2.metric("Orders", f"{total_orders:,}")
col3.metric("AOV", f"${aov:,.2f}")
col4.metric("MoM Growth", f"{growth:.2f}%")

st.markdown("---")

st.subheader("Revenue Trend & 7-Day Rolling Average")
df_filtered = df_filtered.sort_values("order_date")
df_filtered['rolling_avg'] = df_filtered['total_revenue'].rolling(7).mean()
st.line_chart(df_filtered.set_index("order_date")[["total_revenue", "rolling_avg"]])

if not df_filtered.empty:
    best_day = df_filtered.loc[df_filtered['total_revenue'].idxmax()]
    st.info(f"""
    **Insight:**
    - Peak Revenue: **{best_day['order_date'].date()}**
    - Value: **${best_day['total_revenue']:,.0f}**
    """)