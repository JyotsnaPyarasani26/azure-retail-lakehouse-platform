# Data Assets

This project uses the Brazilian E-Commerce Public Dataset by Olist.

Dataset Source:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Source Files Used

- customers
- products
- sellers
- orders
- order_items
- order_payments
- geolocation

## Purpose

The source data is ingested into Azure Databricks and processed through:

- Bronze Layer (raw ingestion)
- Silver Layer (data cleansing and transformation)
- Gold Layer (star schema modeling)
- Business KPI Layer (analytics-ready datasets)

## Data Flow

Kaggle Dataset → Bronze Layer → Silver Layer → Gold Layer → Power BI Dashboards

## Note

The original dataset is not stored in this repository. Download the dataset from Kaggle and upload the source files to Databricks before executing the notebooks.
