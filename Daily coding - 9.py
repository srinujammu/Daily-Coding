# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://www.youtube.com/watch?v=cWNqEWvlkBI
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# MAGIC
# MAGIC For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# COMMAND ----------

lst = [8,2,8,7]
incl =0
excl =0

for i in lst:
  temp = max(incl, excl)
  incl = i + excl
  excl = temp
 # print(temp, incl, excl)

print (incl, excl)


# COMMAND ----------

def adjacent_sum(arr):
    sum = 0
    if len(arr) < 0 or len(arr) == 2:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        if len(arr) % 2 == 0:
            for i in range(0, len(arr), 3):
              sum += arr[i]
        else:
            for i in range(0, len(arr), 2):
              sum += arr[i]
        return sum
# print(adjacent_sum([2, 4, 6, 2, 5]))
print(adjacent_sum([8,2,8,7]))

# COMMAND ----------

# MAGIC %md
# MAGIC Finally :: The code is not accurate