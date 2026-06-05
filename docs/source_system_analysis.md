# Source System Analysis

## Project

Azure Retail Lakehouse Platform

## Business Domain

Brazilian E-Commerce Analytics Platform

## Source System

Olist E-Commerce Dataset

## Source Files

| Source File                       | Description                          |
| --------------------------------- | ------------------------------------ |
| olist_customers_dataset           | Customer master data                 |
| olist_orders_dataset              | Order header information             |
| olist_order_items_dataset         | Order line items                     |
| olist_order_payments_dataset      | Payment transactions                 |
| olist_order_reviews_dataset       | Customer reviews                     |
| olist_products_dataset            | Product master data                  |
| olist_sellers_dataset             | Seller master data                   |
| olist_geolocation_dataset         | Geographic reference data            |
| product_category_name_translation | Product category translation mapping |

## Target Architecture

Bronze Layer

* Raw ingestion

Silver Layer

* Data quality checks
* Standardisation
* Data cleansing

Gold Layer

* Star schema
* Fact tables
* Dimension tables
* KPI layer

## Business KPIs

* Revenue
* Total Orders
* Average Order Value
* Customer Lifetime Value
* Repeat Purchase Rate
* Seller Performance
* Product Performance
* Delivery Performance
* Review Score Analysis
