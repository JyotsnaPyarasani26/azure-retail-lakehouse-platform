# Source to Target Mapping

## Source Tables

### bronze_orders
**Primary Key**
- order_id

### bronze_order_items
**Primary Key**
- order_id
- order_item_id

### bronze_payments
**Primary Key**
- order_id

### bronze_reviews
**Primary Key**
- review_id

### bronze_customers
**Primary Key**
- customer_id

### bronze_products
**Primary Key**
- product_id

### bronze_sellers
**Primary Key**
- seller_id

### bronze_geolocation
**Primary Key**
- geolocation_zip_code_prefix

### bronze_category_translation
**Primary Key**
- product_category_name

---

# Relationships

| Parent Table | Child Table | Join Column |
|-------------|-------------|-------------|
| bronze_customers | bronze_orders | customer_id |
| bronze_orders | bronze_order_items | order_id |
| bronze_orders | bronze_payments | order_id |
| bronze_orders | bronze_reviews | order_id |
| bronze_products | bronze_order_items | product_id |
| bronze_sellers | bronze_order_items | seller_id |
| bronze_category_translation | bronze_products | product_category_name |

---

# Gold Layer Design

## Fact Table

### fact_sales

Contains:
- order_id
- customer_id
- product_id
- seller_id
- payment_value
- freight_value
- order_purchase_timestamp
- order_delivered_customer_date

---

## Dimension Tables

### dim_customer
Contains customer attributes and location information.

### dim_product
Contains product details and translated category names.

### dim_seller
Contains seller information and seller location.

### dim_date
Contains:
- date_key
- day
- month
- quarter
- year
- week

---

# Data Flow

Raw CSV Files
↓

Bronze Layer
- bronze_orders
- bronze_order_items
- bronze_payments
- bronze_reviews
- bronze_customers
- bronze_products
- bronze_sellers
- bronze_geolocation
- bronze_category_translation

↓

Silver Layer
- silver_orders
- silver_customers
- silver_products
- silver_sellers
- silver_payments
- silver_reviews

↓

Gold Layer
- fact_sales
- dim_customer
- dim_product
- dim_seller
- dim_date

↓

Power BI Dashboard
