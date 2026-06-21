# Databricks notebook source
# MAGIC %md
# MAGIC ## **Business KPIs**

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %md
# MAGIC Load Gold Tables

# COMMAND ----------

sales_fact = spark.table("workspace.default.gold_sales_fact")
customer_dim = spark.table("workspace.default.gold_customer_dim")
product_dim = spark.table("workspace.default.gold_product_dim")
seller_dim = spark.table("workspace.default.gold_seller_dim")
date_dim = spark.table("workspace.default.gold_date_dim")

# COMMAND ----------

# MAGIC %md
# MAGIC Executive Summary

# COMMAND ----------

executive_kpis = (
    sales_fact
    .agg(
        round(sum("total_revenue"), 2).alias("total_revenue"),
        countDistinct("order_id").alias("total_orders"),
        countDistinct("customer_id").alias("total_customers"),
        round(avg("payment_value"), 2).alias("avg_order_value"),
        round(avg("delivery_days"), 2).alias("avg_delivery_days"),
        round(avg("is_delivered_late") * 100, 2)
            .alias("late_delivery_pct")
    )
)

display(executive_kpis)

# COMMAND ----------

executive_kpis.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable(
        "workspace.default.kpi_executive_summary"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC Sales By State

# COMMAND ----------

sales_by_state = (
    sales_fact.alias("s")
    .join(
        customer_dim.alias("c"),
        "customer_id"
    )
    .groupBy("customer_state")
    .agg(
        round(sum("total_revenue"),2)
            .alias("total_revenue"),
        countDistinct("order_id")
            .alias("total_orders")
    )
    .orderBy(desc("total_revenue"))
)

display(sales_by_state)

# COMMAND ----------

sales_by_state.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable(
        "workspace.default.kpi_sales_by_state"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC Sales By Category

# COMMAND ----------

sales_by_category = (
    sales_fact.alias("s")
    .join(
        product_dim.alias("p"),
        "product_id"
    )
    .groupBy(
        "product_category_name_english"
    )
    .agg(
        round(sum("total_revenue"),2)
            .alias("total_revenue"),
        countDistinct("order_id")
            .alias("total_orders")
    )
    .orderBy(desc("total_revenue"))
)

display(sales_by_category)

# COMMAND ----------

sales_by_category.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable(
        "workspace.default.kpi_sales_by_category"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC Monthly Sales Trend

# COMMAND ----------

monthly_sales_trend = (
    sales_fact
    .groupBy(
        year("order_purchase_date")
            .alias("year"),
        month("order_purchase_date")
            .alias("month")
    )
    .agg(
        round(sum("total_revenue"),2)
            .alias("monthly_revenue")
    )
    .orderBy("year","month")
)

display(monthly_sales_trend)

# COMMAND ----------

monthly_sales_trend.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable(
        "workspace.default.kpi_monthly_sales_trend"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC Delivery Performance

# COMMAND ----------

delivery_performance = (
    sales_fact
    .groupBy("is_delivered_late")
    .agg(
        count("*").alias("orders")
    )
)

display(delivery_performance)

# COMMAND ----------

delivery_performance.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable(
        "workspace.default.kpi_delivery_performance"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC Final Verification

# COMMAND ----------

spark.sql("SHOW TABLES").show(truncate=False)