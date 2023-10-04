# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://github.com/offamitkumar/Daily-Coding-Problem

# COMMAND ----------

# MAGIC %md
# MAGIC Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# MAGIC
# MAGIC For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# COMMAND ----------

# DBTITLE 1,Basic Sorting with input Data
n = int(input());

y = [];

for i in range(0, n):
  temp = int(input());
  y.append(temp);
  
print(y);
temp1 = y.sort;
print(sorted(y))

# COMMAND ----------

# DBTITLE 1,Basic Coding
def insert_data(n):
  list_var= [];
  for i in range(0,n):
    tempvar = int(input())
    list_var.append(tempvar)
  list_var = sorted(list_var)
  return list_var

n = int(input())
call_fun = insert_data(n)

t = int(input())

for i in range(0, max(call_fun)):
  if i >= t:
    break;
  if i not in call_fun:
    temp = i
print(temp)
  

print(type(call_fun))

