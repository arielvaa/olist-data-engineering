import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(page_title="Retention", layout="wide")

@st.cache_data
def load_data():
    conn = duckdb.connect("olist.db")
    return conn.execute("""
        SELECT 
            c.customer_unique_id,
            o.order_purchase_timestamp::TIMESTAMP as order_time
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
    """).fetchdf()

df = load_data()
with st.sidebar:
    st.header("Kamus Istilah")
    
    with st.expander("Apa itu Cohort?"):
        st.write("""
        **Cohort** adalah sebutan untuk 'Angkatan'. 
        Di sini, pelanggan dikelompokkan berdasarkan bulan pertama kali mereka belanja.
        """)
    
    with st.expander("Apa itu Retensi?"):
        st.write("""
        **Retensi** adalah kemampuan kita menjaga pelanggan agar mau belanja lagi di bulan-bulan berikutnya.
        """)
        
    with st.expander("Bulan ke-0, 1, 2..."):
        st.write("""
        - **Bulan 0:** Bulan saat pelanggan pertama kali beli.
        - **Bulan 1:** Sebulan setelah pembelian pertama.
        - **Bulan 2:** Dua bulan setelahnya, dan seterusnya.
        """)

st.title("Tabel Retensi Pelanggan")
df['order_month'] = df['order_time'].dt.to_period('M')
df['cohort_group'] = df.groupby('customer_unique_id')['order_time'].transform('min').dt.to_period('M')
df['month_index'] = (df['order_month'].view('int64') - df['cohort_group'].view('int64'))
cohort_counts = df.groupby(['cohort_group', 'month_index'])['customer_unique_id'].nunique().reset_index()
retention_table = cohort_counts.pivot(index='cohort_group', columns='month_index', values='customer_unique_id')
cohort_size = retention_table.iloc[:, 0]
retention_pct = retention_table.divide(cohort_size, axis=0)
st.subheader("1. Tabel Jumlah Pelanggan (Angka Asli)")
st.dataframe(retention_table)

st.subheader("2. Tabel Retensi (Dalam %)")
st.dataframe(retention_pct.style.format("{:.2%}", na_rep=""))

st.info("""
**Cara Membaca:**
- Lihat **Baris**: Cari bulan kapan pelanggan bergabung (misal: 2017-01).
- Lihat **Kolom**: Geser ke kanan untuk lihat berapa % yang balik lagi di bulan ke-1, ke-2, dst.
- **Kesimpulan:** Jika kolom 1, 2, dst isinya banyak yang kosong, berarti pelanggan cuma sekali beli saja.
""")