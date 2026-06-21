# Databricks notebook source
# MAGIC %md
# MAGIC ## **Silver Transformations**

# COMMAND ----------

# MAGIC %md
# MAGIC Imports

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
reviews_df = spark.table("workspace.default.bronze_reviews")
payments_df = spark.table("workspace.default.bronze_payments")
order_items_df = spark.table("workspace.default.bronze_order_items")
category_df = spark.table("workspace.default.bronze_category_translation")

# COMMAND ----------

# MAGIC %md
# MAGIC Create Silver Orders

# COMMAND ----------

silver_orders = (
    orders_df
    .filter(col("order_id").isNotNull())
    .dropDuplicates(["order_id"])
    .withColumn("order_status", lower(trim(col("order_status"))))
    .withColumn("order_purchase_date", to_date(col("order_purchase_timestamp")))
    .withColumn("delivery_days", datediff(col("order_delivered_customer_date"), col("order_purchase_timestamp")))
    .withColumn(
        "is_delivered_late",
        when(col("order_delivered_customer_date") > col("order_estimated_delivery_date"), 1).otherwise(0)
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC Save Silver Orders

# COMMAND ----------

silver_orders.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("workspace.default.silver_orders")

# COMMAND ----------

# MAGIC %md
# MAGIC Verify

# COMMAND ----------

display(spark.table("workspace.default.silver_orders").limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC Build Remaining Silver Tables

# COMMAND ----------

silver_customers = (
    customers_df
    .filter(col("customer_id").isNotNull())
    .dropDuplicates(["customer_id"])
)

category_df = spark.table("workspace.default.bronze_category_translation")

silver_products = (
    products_df.alias("p")
    .filter(col("product_id").isNotNull())
    .join(
        category_df.alias("c"),
        "product_category_name",
        "left"
    )
    .dropDuplicates(["product_id"])
)

silver_sellers = (
    sellers_df
    .filter(col("seller_id").isNotNull())
    .dropDuplicates(["seller_id"])
)

silver_reviews = (
    reviews_df
    .filter(col("review_id").isNotNull())
)

# COMMAND ----------

# MAGIC %md
# MAGIC Save Silver Tables

# COMMAND ----------

silver_customers.write.mode("overwrite").format("delta").saveAsTable(
    "workspace.default.silver_customers"
)



silver_sellers.write.mode("overwrite").format("delta").saveAsTable(
    "workspace.default.silver_sellers"
)

silver_reviews.write.mode("overwrite").format("delta").saveAsTable(
    "workspace.default.silver_reviews"
)

# COMMAND ----------

silver_products.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("workspace.default.silver_products")

# COMMAND ----------

spark.table("workspace.default.silver_products").printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC Verify

# COMMAND ----------

spark.sql("SHOW TABLES").show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC build the key Silver joined table- silver_sales_transactions

# COMMAND ----------

silver_sales_transactions = (
    order_items_df.alias("oi")
    .join(silver_orders.alias("o"), col("oi.order_id") == col("o.order_id"), "inner")
    .join(silver_products.alias("p"), col("oi.product_id") == col("p.product_id"), "left")
    .join(silver_sellers.alias("s"), col("oi.seller_id") == col("s.seller_id"), "left")
    .join(payments_df.alias("pay"), col("oi.order_id") == col("pay.order_id"), "left")
    .join(category_df.alias("cat"), col("p.product_category_name") == col("cat.product_category_name"), "left")
    .select(
        col("oi.order_id"),
        col("oi.order_item_id"),
        col("o.customer_id"),
        col("oi.product_id"),
        col("oi.seller_id"),
        col("o.order_status"),
        col("o.order_purchase_date"),
        col("o.delivery_days"),
        col("o.is_delivered_late"),
        col("p.product_category_name"),
        col("cat.product_category_name_english"),
        col("pay.payment_type"),
        col("pay.payment_value"),
        col("oi.price").alias("item_price"),
        col("oi.freight_value")
    )
)

# COMMAND ----------

silver_sales_transactions.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("workspace.default.silver_sales_transactions")

# COMMAND ----------

display(
    spark.table("workspace.default.silver_sales_transactions").limit(10)
)

# COMMAND ----------

spark.sql("""
SHOW TABLES IN workspace.default
""").display()