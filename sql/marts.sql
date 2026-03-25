CREATE OR REPLACE TABLE sales_mart AS
SELECT
	DATE(order_purchase_timestamp) as order_date,
	COUNT(order_id) as total_orders,
	SUM(total_payment) as total_revenue,
	AVG(total_payment) as avg_order_value
FROM fact_orders
GROUP BY 1

CREATE OR REPLACE TABLE customer_mart AS
SELECT
	customer_id,
	COUNT(order_id) as total_orders,
	SUM(total_payment) as total_spent,
	AVG(avg_review_score) as avg_review
FROM fact_orders
GROUP BY customer_id

CREATE OR REPLACE TABLE product_mart AS
SELECT
	p.category,
	COUNT(oi.order_id) as total_orders,
	SUM(oi.price) as total_revenue
FROM order_items oi
JOIN dim_products p ON oi.product_id = p.product_id
GROUP BY p.category