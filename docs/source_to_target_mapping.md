Source to Target Mapping
Source Tables
bronze_orders

Primary Key:

order_id
bronze_order_items

Primary Key:

order_id
order_item_id
bronze_payments

Primary Key:

order_id
bronze_reviews

Primary Key:

review_id
bronze_customers

Primary Key:

customer_id
bronze_products

Primary Key:

product_id
bronze_sellers

Primary Key:

seller_id
bronze_geolocation

Primary Key:

geolocation_zip_code_prefix
bronze_category_translation

Primary Key:

product_category_name
Relationships

orders.customer_id
→ customers.customer_id

order_items.order_id
→ orders.order_id

order_items.product_id
→ products.product_id

order_items.seller_id
→ sellers.seller_id

payments.order_id
→ orders.order_id

reviews.order_id
→ orders.order_id

products.product_category_name
→ category_translation.product_category_name

Gold Layer Design

Fact Table:

fact_sales

Dimension Tables:

dim_customer
dim_product
dim_seller
dim_date
