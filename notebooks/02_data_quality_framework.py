# Databricks notebook source
# MAGIC %md
# MAGIC ### # **Data Quality Framework**

# COMMAND ----------

# MAGIC %md
# MAGIC Import Libraries

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC Load Bronze Tables

# COMMAND ----------

orders_df = spark.table("workspace.default.bronze_orders")
customers_df = spark.table("workspace.default.bronze_customers")
products_df = spark.table("workspace.default.bronze_products")
sellers_df = spark.table("workspace.default.bronze_sellers")
payments_df = spark.table("workspace.default.bronze_payments")
reviews_df = spark.table("workspace.default.bronze_reviews")
order_items_df = spark.table("workspace.default.bronze_order_items")
geolocation_df = spark.table("workspace.default.bronze_geolocation")
category_df = spark.table("workspace.default.bronze_category_translation")

# COMMAND ----------

# MAGIC %md
# MAGIC Verify Tables Loaded

# COMMAND ----------

print("Orders:", orders_df.count())
print("Customers:", customers_df.count())
print("Products:", products_df.count())
print("Sellers:", sellers_df.count())
print("Payments:", payments_df.count())
print("Reviews:", reviews_df.count())
print("Order Items:", order_items_df.count())
print("Geolocation:", geolocation_df.count())
print("Category Translation:", category_df.count())

# COMMAND ----------

# MAGIC %md
# MAGIC Define Primary Keys

# COMMAND ----------

primary_keys = {
    "bronze_orders": "order_id",
    "bronze_customers": "customer_id",
    "bronze_products": "product_id",
    "bronze_sellers": "seller_id",
    "bronze_reviews": "review_id"
}

# COMMAND ----------

# MAGIC %md
# MAGIC Null Primary Key Check

# COMMAND ----------

tables = {
    "bronze_orders": orders_df,
    "bronze_customers": customers_df,
    "bronze_products": products_df,
    "bronze_sellers": sellers_df,
    "bronze_reviews": reviews_df
}

for table_name, df in tables.items():

    pk = primary_keys[table_name]

    null_count = df.filter(col(pk).isNull()).count()

    print(
        f"{table_name} | NULL {pk}: {null_count}"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC Duplicate Primary Key Check

# COMMAND ----------

for table_name, df in tables.items():

    pk = primary_keys[table_name]

    duplicate_count = (
        df.groupBy(pk)
          .count()
          .filter(col("count") > 1)
          .count()
    )

    print(
        f"{table_name} | DUPLICATES: {duplicate_count}"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC Quality Summary

# COMMAND ----------

from pyspark.sql import Row

# COMMAND ----------

quality_results = []

for table_name, df in tables.items():

    if table_name not in primary_keys:
        continue

    pk = primary_keys[table_name]

    total_rows = df.count()

    null_count = (
        df.filter(col(pk).isNull())
          .count()
    )

    duplicate_count = (
        df.groupBy(pk)
          .count()
          .filter(col("count") > 1)
          .count()
    )

    quality_results.append(
        Row(
            table_name=table_name,
            total_rows=total_rows,
            null_primary_keys=null_count,
            duplicate_primary_keys=duplicate_count
        )
    )

# COMMAND ----------

# MAGIC %md
# MAGIC Create Quality Dashboard Table

# COMMAND ----------

quality_df = spark.createDataFrame(quality_results)

display(
    quality_df
)

# COMMAND ----------

quality_df.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.data_quality_audit")

# COMMAND ----------

display(
    spark.table("workspace.default.data_quality_audit")
)