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

# Data Dictionary

This document describes all Bronze, Silver, and Gold layer tables used in the Azure Retail Lakehouse Platform.

---

# Bronze Layer Tables

## bronze_orders

| Column | Data Type | Description |
|----------|----------|-------------|
| order_id | string | Unique order identifier |
| customer_id | string | Customer identifier |
| order_status | string | Order status |
| order_purchase_timestamp | timestamp | Order purchase timestamp |
| order_approved_at | timestamp | Order approval timestamp |
| order_delivered_carrier_date | timestamp | Date order was handed to carrier |
| order_delivered_customer_date | timestamp | Date order was delivered to customer |
| order_estimated_delivery_date | timestamp | Estimated delivery date |

---

## bronze_customers

| Column | Data Type | Description |
|----------|----------|-------------|
| customer_id | string | Customer identifier |
| customer_unique_id | string | Unique customer identifier |
| customer_zip_code_prefix | integer | Customer ZIP code prefix |
| customer_city | string | Customer city |
| customer_state | string | Customer state |

---

## bronze_products

| Column | Data Type | Description |
|----------|----------|-------------|
| product_id | string | Product identifier |
| product_category_name | string | Product category |
| product_name_length | integer | Product name length |
| product_description_length | integer | Product description length |
| product_photos_qty | integer | Number of product photos |
| product_weight_g | integer | Product weight in grams |
| product_length_cm | integer | Product length in cm |
| product_height_cm | integer | Product height in cm |
| product_width_cm | integer | Product width in cm |

---

## bronze_sellers

| Column | Data Type | Description |
|----------|----------|-------------|
| seller_id | string | Seller identifier |
| seller_zip_code_prefix | integer | Seller ZIP code prefix |
| seller_city | string | Seller city |
| seller_state | string | Seller state |

---

## bronze_reviews

| Column | Data Type | Description |
|----------|----------|-------------|
| review_id | string | Review identifier |
| order_id | string | Order identifier |
| review_score | integer | Customer review score |
| review_comment_title | string | Review title |
| review_comment_message | string | Review comment |
| review_creation_date | timestamp | Review creation date |
| review_answer_timestamp | timestamp | Review response timestamp |

---

## bronze_payments

| Column | Data Type | Description |
|----------|----------|-------------|
| order_id | string | Order identifier |
| payment_sequential | integer | Payment sequence number |
| payment_type | string | Payment method |
| payment_installments | integer | Number of installments |
| payment_value | decimal | Payment amount |

---

## bronze_order_items

| Column | Data Type | Description |
|----------|----------|-------------|
| order_id | string | Order identifier |
| order_item_id | integer | Order item number |
| product_id | string | Product identifier |
| seller_id | string | Seller identifier |
| shipping_limit_date | timestamp | Shipping deadline |
| price | decimal | Product price |
| freight_value | decimal | Freight cost |

---

## bronze_geolocation

| Column | Data Type | Description |
|----------|----------|-------------|
| geolocation_zip_code_prefix | integer | ZIP code prefix |
| geolocation_lat | double | Latitude |
| geolocation_lng | double | Longitude |
| geolocation_city | string | City |
| geolocation_state | string | State |

---

## bronze_category_translation

| Column | Data Type | Description |
|----------|----------|-------------|
| product_category_name | string | Original category name |
| product_category_name_english | string | English category name |

---

# Silver Layer Tables

## silver_orders

Business-ready order data enriched with delivery KPIs.

| Column | Description |
|----------|-------------|
| order_id | Order identifier |
| customer_id | Customer identifier |
| order_status | Order status |
| order_purchase_date | Purchase date |
| delivery_days | Number of days taken for delivery |
| is_delivered_late | Late delivery flag |

---

## silver_customers

Customer master data.

| Column | Description |
|----------|-------------|
| customer_id | Customer identifier |
| customer_unique_id | Unique customer identifier |
| customer_city | Customer city |
| customer_state | Customer state |

---

## silver_products

Product master data enriched with English category names.

| Column | Description |
|----------|-------------|
| product_id | Product identifier |
| product_category_name | Original category name |
| product_category_name_english | English category name |
| product_weight_g | Product weight |
| product_length_cm | Product length |
| product_height_cm | Product height |
| product_width_cm | Product width |

---

## silver_sellers

Seller master data.

| Column | Description |
|----------|-------------|
| seller_id | Seller identifier |
| seller_city | Seller city |
| seller_state | Seller state |

---

## silver_reviews

Review data prepared for analytics.

| Column | Description |
|----------|-------------|
| review_id | Review identifier |
| order_id | Order identifier |
| review_score | Customer review score |

---

## silver_sales_transactions

Integrated sales transaction dataset created by joining orders, products, sellers, and payments.

| Column | Description |
|----------|-------------|
| order_id | Order identifier |
| customer_id | Customer identifier |
| product_id | Product identifier |
| seller_id | Seller identifier |
| payment_type | Payment method |
| payment_value | Payment amount |
| item_price | Product price |
| freight_value | Freight amount |
| delivery_days | Delivery duration |
| is_delivered_late | Late delivery indicator |

---

# Gold Layer Tables

## gold_sales_fact

Central business fact table used for sales analytics and dashboard reporting.

| Column | Description |
|----------|-------------|
| order_id | Order identifier |
| customer_id | Customer identifier |
| product_id | Product identifier |
| seller_id | Seller identifier |
| payment_type | Payment method |
| payment_value | Payment amount |
| item_price | Product price |
| freight_value | Freight amount |
| total_revenue | Total revenue generated |
| delivery_days | Delivery duration |
| is_delivered_late | Delivery SLA indicator |

---

## gold_customer_dim

Customer dimension table.

| Column | Description |
|----------|-------------|
| customer_id | Customer identifier |
| customer_unique_id | Unique customer identifier |
| customer_city | Customer city |
| customer_state | Customer state |

---

## gold_product_dim

Product dimension table.

| Column | Description |
|----------|-------------|
| product_id | Product identifier |
| product_category_name | Original category |
| product_category_name_english | English category |
| product_weight_g | Product weight |
| product_length_cm | Product length |
| product_height_cm | Product height |
| product_width_cm | Product width |

---

## gold_seller_dim

Seller dimension table.

| Column | Description |
|----------|-------------|
| seller_id | Seller identifier |
| seller_city | Seller city |
| seller_state | Seller state |

---

## gold_date_dim

Date dimension used for time-series analysis.

| Column | Description |
|----------|-------------|
| date_key | Surrogate date key (YYYYMMDD) |
| full_date | Calendar date |
| year | Calendar year |
| quarter | Calendar quarter |
| month | Calendar month |
| month_name | Month name |
| week | Week number |
| day | Day of month |

---
