# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
# MAGIC
# MAGIC
# MAGIC Given an array nums of size n, return the majority element.
# MAGIC
# MAGIC The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# MAGIC

# COMMAND ----------


import operator
list = [2,2,2,2,1,1,1,2,2,3,1,1]
dict = {i:list.count(i) for i in list}
print(max(dict.items(), key=operator.itemgetter(1))[0])



# COMMAND ----------

class solution:
  def majorityElement(self, nums: List[int]) -> int:
    return counter(nums).most_common()[0][0]
