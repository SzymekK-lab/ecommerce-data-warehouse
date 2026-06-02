WITH customer_revenue AS (
    SELECT
        c.customer_name,
        SUM(f.total_amount) revenue
    FROM fact_sales f
    JOIN dim_customer c
        ON c.customer_id = f.customer_id
    GROUP BY c.customer_name
)
SELECT *
FROM customer_revenue
ORDER BY revenue DESC
LIMIT 10;

SELECT
    c.customer_name,
    SUM(f.total_amount) revenue,
    DENSE_RANK() OVER(
        ORDER BY SUM(f.total_amount) DESC
    ) rank
FROM fact_sales f
JOIN dim_customer c
    ON c.customer_id = f.customer_id
GROUP BY c.customer_name;