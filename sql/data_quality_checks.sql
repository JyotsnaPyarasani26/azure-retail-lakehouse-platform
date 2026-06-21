-- Duplicate Customer Check

SELECT
    customer_id,
    COUNT(*) AS duplicate_count
FROM bronze_customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
