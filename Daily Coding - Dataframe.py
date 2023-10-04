# Databricks notebook source
# MAGIC %md
# MAGIC ###Dataframe

# COMMAND ----------

spark.version
from pyspark.sql import SparkSession
spark2 = SparkSession.newSession

# COMMAND ----------

# Pandas dataframe
columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]


# COMMAND ----------

spark = SparkSession.builder.appName('SparkbySrini.com').getOrCreate()
rdd = spark.sparkContext.parallelize(data)

# COMMAND ----------

# Convert from RDD To Spark DF

dfrddtodf= rdd.toDF()

# COMMAND ----------

# adding columns 

colunns = ['Language', 'price']
dfrddtodf = rdd.toDF(columns)
dfrddtodf.printSchema()
display(dfrddtodf)

# COMMAND ----------

## dataframe using createDataFrame

dfFromData2 = spark.createDataFrame(data).toDF(*columns)
display(dfFromData2)

# COMMAND ----------

from pyspark.sql import Row
rowData = map(lambda x: Row(*x), data) 
dfFromData3 = spark.createDataFrame(rowData,columns)


# COMMAND ----------

# MAGIC %md
# MAGIC Reference Link : https://sparkbyexamples.com/pyspark/different-ways-to-create-dataframe-in-pyspark/