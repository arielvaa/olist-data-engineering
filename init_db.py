import duckdb

conn = duckdb.connect("olist.db")
conn.execute("""
CREATE OR REPLACE TABLE customers AS 
SELECT * FROM read_csv_auto('data/raw/olist_customers_dataset.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE orders AS 
SELECT * FROM read_csv_auto('data/raw/olist_orders_dataset.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE order_items AS 
SELECT * FROM read_csv_auto('data/raw/olist_order_items_dataset.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE payments AS 
SELECT * FROM read_csv_auto('data/raw/olist_order_payments_dataset.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE reviews AS 
SELECT * FROM read_csv_auto('data/raw/olist_order_reviews_dataset.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE products AS 
SELECT * FROM read_csv_auto('data/raw/olist_products_dataset.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE sellers AS 
SELECT * FROM read_csv_auto('data/raw/olist_sellers_dataset.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE geolocation AS 
SELECT * FROM read_csv_auto('data/raw/olist_geolocation_dataset.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE category_translation AS 
SELECT * FROM read_csv_auto('data/raw/product_category_name_translation.csv');
""")

conn.execute("""
CREATE OR REPLACE TABLE sales_mart AS
SELECT 
    DATE(order_purchase_timestamp) as order_date,
    COUNT(order_id) as total_orders,
    SUM(payment_value) as total_revenue,
    AVG(payment_value) as avg_order_value
FROM orders o
JOIN payments p ON o.order_id = p.order_id
GROUP BY 1;
""")

conn.execute("""
CREATE OR REPLACE TABLE customer_mart AS
SELECT 
    customer_id,
    COUNT(order_id) as total_orders,
    SUM(payment_value) as total_spent
FROM orders o
JOIN payments p ON o.order_id = p.order_id
GROUP BY customer_id;
""")

conn.execute("""
CREATE OR REPLACE TABLE product_mart AS
SELECT 
    product_id,
    COUNT(order_id) as total_orders,
    SUM(price) as total_revenue
FROM order_items
GROUP BY product_id;
""")

print("DB initialized!")