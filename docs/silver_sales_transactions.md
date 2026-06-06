# Silver Sales Transactions

## Purpose

Create a business-ready transaction table by joining orders, order items, products, sellers, payments and category translation data.

## Source Tables

- silver_orders
- silver_products
- silver_sellers
- bronze_order_items
- bronze_payments
- bronze_category_translation

## Output Table

workspace.default.silver_sales_transactions

## Business Logic

- Joined order line items with order header data
- Added customer, product and seller identifiers
- Added product category translation
- Added payment method and payment value
- Added delivery performance fields
- Prepared transaction-level data for Gold Star Schema

## Key Columns

- order_id
- order_item_id
- customer_id
- product_id
- seller_id
- order_status
- order_purchase_date
- delivery_days
- is_delivered_late
- product_category_name
- product_category_name_english
- payment_type
- payment_value
- item_price
- freight_value

## Next Layer

This table will feed:

- gold_sales_fact
- gold_customer_dim
- gold_product_dim
- gold_seller_dim
- gold_date_dim
