import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://admin:admin@localhost:5432/ecommerce"
)

print("Loading CSV files...")

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
dates = pd.read_csv("data/dates.csv")
sales = pd.read_csv("data/sales.csv")

print("CSV files loaded")

with engine.begin() as conn:
    conn.exec_driver_sql("TRUNCATE TABLE fact_sales RESTART IDENTITY CASCADE")
    conn.exec_driver_sql("TRUNCATE TABLE dim_customer RESTART IDENTITY CASCADE")
    conn.exec_driver_sql("TRUNCATE TABLE dim_product RESTART IDENTITY CASCADE")
    conn.exec_driver_sql("TRUNCATE TABLE dim_date RESTART IDENTITY CASCADE")

print("Tables truncated")

customers.to_sql(
    "dim_customer",
    engine,
    if_exists="append",
    index=False
)

products.to_sql(
    "dim_product",
    engine,
    if_exists="append",
    index=False
)

dates.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)

print("Dimensions loaded")

sales.to_sql(
    "fact_sales",
    engine,
    if_exists="append",
    index=False
)

print("Fact table loaded")

print("ETL completed successfully")