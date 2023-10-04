# Databricks notebook source
# MAGIC %md
# MAGIC ###DBUtils

# COMMAND ----------

spark.version
from pyspark.sql import SparkSession
spark2 = SparkSession.newSession

# COMMAND ----------

from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession
 
spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

# COMMAND ----------

display(dbutils.fs.mounts())