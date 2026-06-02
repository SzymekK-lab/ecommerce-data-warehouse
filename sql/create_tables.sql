CREATE TABLE dim_customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100)
);

CREATE TABLE dim_product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(100),
    price NUMERIC(10,2)
);

CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER
);

CREATE TABLE fact_sales (
    sale_id SERIAL PRIMARY KEY,

    customer_id INTEGER REFERENCES dim_customer(customer_id),

    product_id INTEGER REFERENCES dim_product(product_id),

    date_id INTEGER REFERENCES dim_date(date_id),

    quantity INTEGER,

    total_amount NUMERIC(10,2)
);