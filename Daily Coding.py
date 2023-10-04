# Databricks notebook source
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

rdds = spark.sparkContext.parallelize([("Mumbai",1)])

# COMMAND ----------

rdds.collect()

# COMMAND ----------

rdds.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Create DataFrame from RDD

# COMMAND ----------

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

import datetime
from datetime import date, datetime

# COMMAND ----------

rdd = spark.sparkContext.parallelize([(1,1.0,"String1",date(2021,1,1), datetime(2021,1,1,12,0)), (2,2.0,"String2",date(2021,2,1), datetime(2021,2,1,12,0)), (2,2.0,"String3",date(2021,3,1), datetime(2021,3,1,12,0))])

# COMMAND ----------

rdd.collect()

# COMMAND ----------

df = spark.createDataFrame(rdd,schema=["num", "float","Str","Dt", "Dttm"])

# COMMAND ----------

df.show()