# Databricks notebook source
# Set Database

spark.sql("USE workspace.default")

# Verify available tables

spark.sql("SHOW TABLES").show(truncate=False)

# COMMAND ----------

orders_df = spark.table("workspace.default.bronze_orders")

display(orders_df.limit(10))

# COMMAND ----------

orders_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

orders_bronze_enriched = (
    orders_df
    .withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )
    .withColumn(
        "source_system",
        lit("OLIST_ECOMMERCE")
    )
    .withColumn(
        "load_date",
        current_date()
    )
)

# COMMAND ----------

orders_bronze_enriched = (
    orders_bronze_enriched
    .withColumn(
        "record_hash",
        sha2(
            concat_ws(
                "||",
                *orders_df.columns
            ),
            256
        )
    )
)

# COMMAND ----------

display(
    orders_bronze_enriched.limit(10)
)