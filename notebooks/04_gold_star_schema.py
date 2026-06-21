# Databricks notebook source
# MAGIC %md
# MAGIC ## **Gold Star Schema**

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC Load Silver Table

# COMMAND ----------

sales_df = spark.table("workspace.default.silver_sales_transactions")
customers_df = spark.table("workspace.default.silver_customers")
products_df = spark.table("workspace.default.silver_products")
sellers_df = spark.table("workspace.default.silver_sellers")

# COMMAND ----------

# MAGIC %md
# MAGIC Gold Sales Fact

# COMMAND ----------

gold_sales_fact = (
    sales_df
    .withColumn("total_revenue", round(col("item_price") + col("freight_value"), 2))
    .withColumn("date_key", date_format(col("order_purchase_date"), "yyyyMMdd").cast("int"))
    .select(
        "order_id",
        "order_item_id",
        "customer_id",
        "product_id",
        "seller_id",
        "date_key",
        "order_purchase_date",
        "payment_type",
        "payment_value",
        "item_price",
        "freight_value",
        "total_revenue",
        "delivery_days",
        "is_delivered_late"
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC Save Fact Table

# COMMAND ----------

gold_sales_fact.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("workspace.default.gold_sales_fact")

# COMMAND ----------

# MAGIC %md
# MAGIC Verify

# COMMAND ----------

display(spark.table("workspace.default.gold_sales_fact").limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC Create Customer Dimension

# COMMAND ----------

gold_customer_dim = (
    customers_df
    .select(
        "customer_id",
        "customer_unique_id",
        "customer_city",
        "customer_state"
    )
    .dropDuplicates()
)

# COMMAND ----------

gold_customer_dim.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("workspace.default.gold_customer_dim")

# COMMAND ----------

display(
    spark.table(
        "workspace.default.gold_customer_dim"
    ).limit(10)
)

# COMMAND ----------

# MAGIC %md
# MAGIC Product Dimension

# COMMAND ----------

gold_product_dim = (
    products_df
    .select(
        "product_id",
        "product_category_name",
        "product_category_name_english",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    )
    .dropDuplicates()
)

# COMMAND ----------

gold_product_dim.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("workspace.default.gold_product_dim")

# COMMAND ----------

display(
    spark.table(
        "workspace.default.gold_product_dim"
    ).limit(10)
)

# COMMAND ----------

# MAGIC %md
# MAGIC Seller Dimension

# COMMAND ----------

gold_seller_dim = (
    sellers_df
    .select(
        "seller_id",
        "seller_city",
        "seller_state"
    )
    .dropDuplicates()
)

# COMMAND ----------

gold_seller_dim.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("workspace.default.gold_seller_dim")

# COMMAND ----------

display(
    spark.table(
        "workspace.default.gold_seller_dim"
    ).limit(10)
)

# COMMAND ----------

# MAGIC %md
# MAGIC Gold Date Dimension

# COMMAND ----------

gold_date_dim = (
    gold_sales_fact
    .select(col("order_purchase_date").alias("full_date"))
    .filter(col("full_date").isNotNull())
    .dropDuplicates()
    .withColumn("date_key", date_format(col("full_date"), "yyyyMMdd").cast("int"))
    .withColumn("year", year(col("full_date")))
    .withColumn("quarter", quarter(col("full_date")))
    .withColumn("month", month(col("full_date")))
    .withColumn("month_name", date_format(col("full_date"), "MMMM"))
    .withColumn("week", weekofyear(col("full_date")))
    .withColumn("day", dayofmonth(col("full_date")))
)

# COMMAND ----------

gold_date_dim.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("workspace.default.gold_date_dim")

# COMMAND ----------

display(
    spark.table("workspace.default.gold_date_dim").orderBy("full_date").limit(10)
)

# COMMAND ----------

spark.sql("SHOW TABLES").show(truncate=False)

# COMMAND ----------

spark.table("workspace.default.gold_sales_fact").count()

# COMMAND ----------

spark.sql("SHOW TABLES").show()