import duckdb
conn = duckdb.connect("C:/Users/arielva/olist-data-engineering/olist.db")
df = conn.execute("SELECT * FROM fact_orders LIMIT 5").fetchdf()
print(df)
tables = conn.execute("SHOW TABLES").fetchall()
print(tables)
df = conn.execute("SELECT * FROM sales_mart LIMIT 5").fetchdf()
print(df)