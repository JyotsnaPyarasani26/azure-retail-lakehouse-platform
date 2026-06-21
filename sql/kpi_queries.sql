-- Business KPIs

SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    SUM(payment_value) AS total_revenue
FROM gold_sales_fact;
