# Databricks Notebooks

This folder contains the PySpark notebooks used to build the Azure Retail Lakehouse Analytics Platform.

## Notebook Execution Flow

### 01_bronze_ingestion.py
Loads raw CSV source files into Bronze Delta tables.

### 02_data_quality_framework.py
Performs null checks, duplicate checks, primary key validation and audit logging.

### 03_silver_transformations.py
Applies business transformations, cleansing and standardization to create Silver tables.

### 04_gold_star_schema.py
Builds Gold layer fact and dimension tables using a star schema design.

### 05_incremental_load_framework.py
Implements Delta MERGE based incremental loading and upsert processing.

### 06_business_kpis.py
Creates business KPI datasets for reporting and analytics.

### 07_pipeline_monitoring.py
Captures pipeline execution logs, run status tracking and monitoring metrics.

## Technologies Used

- Azure Databricks
- PySpark
- Delta Lake
- SQL
- Medallion Architecture
