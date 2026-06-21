# Databricks notebook source
# MAGIC %md
# MAGIC ## **Pipeline Monitoring**

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
from datetime import datetime

# COMMAND ----------

# MAGIC %md
# MAGIC Create pipeline run log

# COMMAND ----------

pipeline_run_log = [
    ("01_bronze_ingestion", "SUCCESS", "Loaded raw Bronze tables"),
    ("02_data_quality_framework", "SUCCESS", "Generated data quality audit"),
    ("03_silver_transformations", "SUCCESS", "Created Silver business tables"),
    ("04_gold_star_schema", "SUCCESS", "Created Gold fact and dimension tables"),
    ("05_incremental_load_framework", "SUCCESS", "Demonstrated Delta MERGE upsert"),
    ("06_business_kpis", "SUCCESS", "Created KPI reporting tables")
]

pipeline_log_df = spark.createDataFrame(
    pipeline_run_log,
    ["notebook_name", "run_status", "run_description"]
).withColumn(
    "run_timestamp",
    current_timestamp()
)

# COMMAND ----------

# MAGIC %md
# MAGIC Save monitoring table

# COMMAND ----------

pipeline_log_df.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("workspace.default.pipeline_run_log")

# COMMAND ----------

# MAGIC %md
# MAGIC Verify

# COMMAND ----------

display(
    spark.table("workspace.default.pipeline_run_log")
)

# COMMAND ----------

spark.table("workspace.default.gold_sales_fact") \
    .toPandas() \
    .to_csv("/tmp/gold_sales_fact.csv", index=False)

# COMMAND ----------

spark.table("workspace.default.gold_customer_dim") \
    .toPandas() \
    .to_csv("/tmp/gold_customer_dim.csv", index=False)

# COMMAND ----------

spark.table("workspace.default.gold_product_dim") \
    .toPandas() \
    .to_csv("/tmp/gold_product_dim.csv", index=False)

# COMMAND ----------

spark.table("workspace.default.gold_seller_dim") \
    .toPandas() \
    .to_csv("/tmp/gold_seller_dim.csv", index=False)

# COMMAND ----------

spark.table("workspace.default.gold_date_dim") \
    .toPandas() \
    .to_csv("/tmp/gold_date_dim.csv", index=False)

# COMMAND ----------

display(spark.table("workspace.default.gold_sales_fact"))

# COMMAND ----------

display(spark.table("workspace.default.gold_customer_dim"))

# COMMAND ----------

display(spark.table("workspace.default.gold_product_dim"))

# COMMAND ----------

display(spark.table("workspace.default.gold_seller_dim"))

# COMMAND ----------

display(spark.table("workspace.default.gold_date_dim"))