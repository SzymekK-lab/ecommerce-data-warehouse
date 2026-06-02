from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker()

NUM_CUSTOMERS = 100
NUM_SALES = 5000

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

customers = []

for _ in range(NUM_CUSTOMERS):
    customers.append({
        "customer_name": fake.name(),
        "city": fake.city(),
        "country": fake.country()
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    DATA_DIR / "customers.csv",
    index=False
)

products = [
    ["Laptop", "Electronics", 4000],
    ["Monitor", "Electronics", 1200],
    ["Keyboard", "Accessories", 200],
    ["Mouse", "Accessories", 150],
    ["Headphones", "Accessories", 350],
    ["Smartphone", "Electronics", 3000]
]

products_df = pd.DataFrame(
    products,
    columns=[
        "product_name",
        "category",
        "price"
    ]
)

products_df.to_csv(
    DATA_DIR / "products.csv",
    index=False
)

dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31"
)

dates_df = pd.DataFrame({
    "full_date": dates
})

dates_df["year"] = dates_df["full_date"].dt.year
dates_df["month"] = dates_df["full_date"].dt.month
dates_df["quarter"] = dates_df["full_date"].dt.quarter

dates_df.to_csv(
    DATA_DIR / "dates.csv",
    index=False
)

product_prices = {
    1: 4000,
    2: 1200,
    3: 200,
    4: 150,
    5: 350,
    6: 3000
}

sales = []

for _ in range(NUM_SALES):

    product_id = random.randint(1, 6)

    quantity = random.randint(1, 5)

    sales.append({
        "customer_id": random.randint(1, NUM_CUSTOMERS),
        "product_id": product_id,
        "date_id": random.randint(1, len(dates_df)),
        "quantity": quantity,
        "total_amount": quantity * product_prices[product_id]
    })

sales_df = pd.DataFrame(sales)

sales_df.to_csv(
    DATA_DIR / "sales.csv",
    index=False
)



print("Data generated successfully")
print(f"Customers: {len(customers_df)}")
print(f"Products: {len(products_df)}")
print(f"Dates: {len(dates_df)}")
print(f"Sales: {len(sales_df)}")