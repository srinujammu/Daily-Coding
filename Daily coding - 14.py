# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
# MAGIC
# MAGIC  1071. Greatest Common Divisor of Strings
# MAGIC
# MAGIC
# MAGIC For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# MAGIC
# MAGIC Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# MAGIC
# MAGIC  
# MAGIC

# COMMAND ----------

temp = "ababab"/"ab"