import duckdb

conn = duckdb.connect("C:/Users/arielva/olist-data-engineering/olist.db")

conn.execute("""
CREATE OR REPLACE TABLE dim_customers AS
SELECT DISTINCT
	customer_id,
	customer_unique_id,
	customer_zip_code_prefix,
	customer_city,
	customer_state
FROM customers
""")

conn.execute("""
CREATE OR REPLACE TABLE dim_products AS
SELECT
	p.product_id,
	t.product_category_name_english as category,
	p.product_weight_g,
	p.product_length_cm,
	p.product_height_cm,
	p.product_width_cm
FROM products p
LEFT JOIN category_translation t
ON p.product_category_name = t.product_category_name
""")

conn.execute("""
CREATE OR REPLACE TABLE dim_sellers AS
SELECT DISTINCT
	seller_id,
	seller_zip_code_prefix,
	seller_city,
	seller_state
FROM sellers
""")

conn.execute("""
CREATE OR REPLACE TABLE dim_location AS
SELECT DISTINCT
	geolocation_zip_code_prefix,
	geolocation_city,
	geolocation_state
FROM geolocation
""")

conn.execute("""
CREATE OR REPLACE TABLE dim_time AS
SELECT DISTINCT
	DATE(order_purchase_timestamp) as date,
	EXTRACT(year FROM order_purchase_timestamp::TIMESTAMP) as year,
	EXTRACT(month FROM order_purchase_timestamp::TIMESTAMP) as month,
	EXTRACT(day FROM order_purchase_timestamp::TIMESTAMP) as day
FROM orders
""")

print(f"semua dimension table berhasil dibuat")