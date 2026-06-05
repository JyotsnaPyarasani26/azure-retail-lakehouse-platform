# Target Data Model

## Gold Layer Star Schema

### Fact Table

#### fact_sales

| Column        |
| ------------- |
| order_id      |
| customer_id   |
| product_id    |
| seller_id     |
| order_date    |
| payment_type  |
| quantity      |
| item_price    |
| freight_value |
| total_revenue |
| review_score  |

---

## Dimension Tables

### dim_customer

| Column             |
| ------------------ |
| customer_id        |
| customer_unique_id |
| customer_city      |
| customer_state     |

---

### dim_product

| Column            |
| ----------------- |
| product_id        |
| product_category  |
| product_weight_g  |
| product_length_cm |
| product_height_cm |
| product_width_cm  |

---

### dim_seller

| Column       |
| ------------ |
| seller_id    |
| seller_city  |
| seller_state |

---

### dim_date

| Column     |
| ---------- |
| date_key   |
| full_date  |
| year       |
| quarter    |
| month      |
| month_name |
| week       |
| day        |

---

## Business KPIs

### Revenue KPIs

* Total Revenue
* Average Order Value
* Revenue by Category
* Revenue by Seller

### Customer KPIs

* Total Customers
* Repeat Customers
* Customer Lifetime Value

### Product KPIs

* Top Products
* Top Categories

### Operational KPIs

* Delivery Performance
* Review Score Analysis
