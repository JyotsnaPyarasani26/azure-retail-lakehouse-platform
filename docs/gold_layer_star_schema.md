# Gold Layer Star Schema

## Purpose

Create reporting-ready fact and dimension tables for analytics and Power BI.

## Fact Table

### gold_sales_fact

Contains transaction-level sales metrics.

Key columns:
- order_id
- order_item_id
- customer_id
- product_id
- seller_id
- order_purchase_date
- payment_type
- payment_value
- item_price
- freight_value
- total_revenue
- delivery_days
- is_delivered_late

## Dimension Tables

### gold_customer_dim
Customer attributes including city and state.

### gold_product_dim
Product attributes including translated product category.

### gold_seller_dim
Seller attributes including city and state.

### gold_date_dim
Date attributes for time-based reporting.

## Star Schema

gold_sales_fact connects to:

- gold_customer_dim using customer_id
- gold_product_dim using product_id
- gold_seller_dim using seller_id
- gold_date_dim using order_purchase_date / full_date

## Business Use Cases

- Revenue analysis
- Product category performance
- Seller performance
- Customer geography analysis
- Delivery performance
- Payment method analysis
