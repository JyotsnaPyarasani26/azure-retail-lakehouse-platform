# Data Dictionary

## Dataset

Olist Brazilian E-Commerce Dataset

## Source Tables

### 1. Customers

**File:** `olist_customers_dataset.csv`

| Column                   | Description                              |
| ------------------------ | ---------------------------------------- |
| customer_id              | Unique ID for each order customer        |
| customer_unique_id       | Unique customer identifier across orders |
| customer_zip_code_prefix | Customer postcode prefix                 |
| customer_city            | Customer city                            |
| customer_state           | Customer state                           |

### 2. Orders

**File:** `olist_orders_dataset.csv`

| Column                        | Description                 |
| ----------------------------- | --------------------------- |
| order_id                      | Unique order identifier     |
| customer_id                   | Customer identifier         |
| order_status                  | Order status                |
| order_purchase_timestamp      | Purchase timestamp          |
| order_approved_at             | Approval timestamp          |
| order_delivered_carrier_date  | Carrier delivery timestamp  |
| order_delivered_customer_date | Customer delivery timestamp |
| order_estimated_delivery_date | Estimated delivery date     |

### 3. Order Items

**File:** `olist_order_items_dataset.csv`

| Column              | Description           |
| ------------------- | --------------------- |
| order_id            | Order identifier      |
| order_item_id       | Line item number      |
| product_id          | Product identifier    |
| seller_id           | Seller identifier     |
| shipping_limit_date | Shipping deadline     |
| price               | Item price            |
| freight_value       | Freight/shipping cost |

### 4. Payments

**File:** `olist_order_payments_dataset.csv`

| Column               | Description             |
| -------------------- | ----------------------- |
| order_id             | Order identifier        |
| payment_sequential   | Payment sequence number |
| payment_type         | Payment method          |
| payment_installments | Number of instalments   |
| payment_value        | Payment amount          |

### 5. Reviews

**File:** `olist_order_reviews_dataset.csv`

| Column                  | Description             |
| ----------------------- | ----------------------- |
| review_id               | Review identifier       |
| order_id                | Order identifier        |
| review_score            | Customer review score   |
| review_comment_title    | Review title            |
| review_comment_message  | Review message          |
| review_creation_date    | Review creation date    |
| review_answer_timestamp | Review answer timestamp |

### 6. Products

**File:** `olist_products_dataset.csv`

| Column                     | Description                    |
| -------------------------- | ------------------------------ |
| product_id                 | Product identifier             |
| product_category_name      | Product category in Portuguese |
| product_name_lenght        | Product name length            |
| product_description_lenght | Product description length     |
| product_photos_qty         | Number of product photos       |
| product_weight_g           | Product weight in grams        |
| product_length_cm          | Product length in cm           |
| product_height_cm          | Product height in cm           |
| product_width_cm           | Product width in cm            |

### 7. Sellers

**File:** `olist_sellers_dataset.csv`

| Column                 | Description            |
| ---------------------- | ---------------------- |
| seller_id              | Seller identifier      |
| seller_zip_code_prefix | Seller postcode prefix |
| seller_city            | Seller city            |
| seller_state           | Seller state           |

### 8. Geolocation

**File:** `olist_geolocation_dataset.csv`

| Column                      | Description     |
| --------------------------- | --------------- |
| geolocation_zip_code_prefix | Postcode prefix |
| geolocation_lat             | Latitude        |
| geolocation_lng             | Longitude       |
| geolocation_city            | City            |
| geolocation_state           | State           |

### 9. Category Translation

**File:** `product_category_name_translation.csv`

| Column                        | Description                    |
| ----------------------------- | ------------------------------ |
| product_category_name         | Product category in Portuguese |
| product_category_name_english | Product category in English    |
