import duckdb

conn = duckdb.connect("C:/Users/arielva/olist-data-engineering/olist.db")

query = """
CREATE OR REPLACE TABLE fact_orders AS
SELECT
	o.order_id,
	o.customer_id,
	o.order_purchase_timestamp,

	-- payment
	SUM(p.payment_value) as total_payment,

	-- review
	AVG(r.review_score) as avg_review_score
FROM orders o

LEFT JOIN payments p
	ON o.order_id = p.order_id
LEFT JOIN reviews r
	ON o.order_id = r.order_id
GROUP BY
	o.order_id,
	o.customer_id,
	o.order_purchase_timestamp
"""

conn.execute(query)
print(f"fact_orders berhasil dibuat")