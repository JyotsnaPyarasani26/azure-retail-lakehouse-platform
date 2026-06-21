# Databricks notebook source
# MAGIC %md
# MAGIC ## **Incremental Load Framework**

# COMMAND ----------

from pyspark.sql.functions import *
from delta.tables import DeltaTable

# COMMAND ----------

bronze_orders = spark.table("workspace.default.bronze_orders")
display(bronze_orders.limit(5))

# COMMAND ----------

# MAGIC %md
# MAGIC Load current Bronze Orders

# COMMAND ----------

bronze_orders = spark.table("workspace.default.bronze_orders")
display(bronze_orders.limit(5))

# COMMAND ----------

# MAGIC %md
# MAGIC Simulate new incoming data

# COMMAND ----------

incoming_orders = (
    bronze_orders
    .limit(10)
    .withColumn("order_status", lit("updated_status"))
    .withColumn("ingestion_timestamp", current_timestamp())
    .withColumn("load_date", current_date())
    .withColumn("source_system", lit("OLIST_ECOMMERCE"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC Add record hash

# COMMAND ----------

incoming_orders = incoming_orders.withColumn(
    "record_hash",
    sha2(concat_ws("||", *bronze_orders.columns), 256)
)

# COMMAND ----------

# MAGIC %md
# MAGIC Create target incremental table

# COMMAND ----------

bronze_orders_incremental = (
    bronze_orders
    .withColumn("ingestion_timestamp", current_timestamp())
    .withColumn("load_date", current_date())
    .withColumn("source_system", lit("OLIST_ECOMMERCE"))
    .withColumn(
        "record_hash",
        sha2(concat_ws("||", *bronze_orders.columns), 256)
    )
)

bronze_orders_incremental.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("workspace.default.bronze_orders_incremental")

# COMMAND ----------

# MAGIC %md
# MAGIC MERGE / UPSERT

# COMMAND ----------

target_table = DeltaTable.forName(
    spark,
    "workspace.default.bronze_orders_incremental"
)

target_table.alias("target").merge(
    incoming_orders.alias("source"),
    "target.order_id = source.order_id"
).whenMatchedUpdate(
    condition="target.record_hash <> source.record_hash",
    set={
        "order_status": "source.order_status",
        "ingestion_timestamp": "source.ingestion_timestamp",
        "load_date": "source.load_date",
        "source_system": "source.source_system",
        "record_hash": "source.record_hash"
    }
).whenNotMatchedInsertAll() \
 .execute()

# COMMAND ----------

# MAGIC %md
# MAGIC Verify update

# COMMAND ----------

display(
    spark.table("workspace.default.bronze_orders_incremental")
    .filter(col("order_status") == "updated_status")
)