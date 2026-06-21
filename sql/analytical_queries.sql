-- Top Product Categories by Revenue

SELECT
    product_category_name_english,
    SUM(payment_value) AS total_revenue
FROM gold_sales_fact
GROUP BY product_category_name_english
ORDER BY total_revenue DESC;
