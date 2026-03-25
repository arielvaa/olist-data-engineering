import duckdb
import pandas as pd
import os

conn = duckdb.connect("../olist.db")

files = {
    "customers": "C:/Users/arielva/olist-data-engineering/data/raw/olist_customers_dataset.csv",
    "geolocation": "C:/Users/arielva/olist-data-engineering/data/raw/olist_geolocation_dataset.csv",
    "order_items": "C:/Users/arielva/olist-data-engineering/data/raw/olist_order_items_dataset.csv",
    "payments": "C:/Users/arielva/olist-data-engineering/data/raw/olist_order_payments_dataset.csv",
    "reviews": "C:/Users/arielva/olist-data-engineering/data/raw/olist_order_reviews_dataset.csv",
    "orders": "C:/Users/arielva/olist-data-engineering/data/raw/olist_orders_dataset.csv",
    "products": "C:/Users/arielva/olist-data-engineering/data/raw/olist_products_dataset.csv",
    "sellers": "C:/Users/arielva/olist-data-engineering/data/raw/olist_sellers_dataset.csv",
    "category_translation": "C:/Users/arielva/olist-data-engineering/data/raw/product_category_name_translation.csv"
}


for table_name, file_path in files.items():
	print(f"loading {table_name}...")
	
	if not os.path.exists(file_path):
		print(f"file tidak ditemukan: {file_path}")
		continue
	df = pd.read_csv(file_path)
	conn.execute(f"""
		CREATE OR REPLACE TABLE {table_name} AS
		SELECT * FROM df
	""")

	print(f"{table_name} loaded ({len(df)} rows)")
print(f"semua data berhasil di-ingest")