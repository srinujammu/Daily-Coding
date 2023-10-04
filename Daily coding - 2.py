# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://github.com/offamitkumar/Daily-Coding-Problem

# COMMAND ----------

Problem 2

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of

the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].

If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# COMMAND ----------

# DBTITLE 1,Option 1: Basic Example
# list of items
list2 = ['cat', 'bat', 'mat', 'cat', 'pet']

print(list2[2])

# COMMAND ----------

# DBTITLE 1,Option 2: Using For loop
for i in range(0, len(list2)):
  print(list2[i])


# COMMAND ----------

# DBTITLE 1,Option 3: Using For Function
def loopfuc( listvar):
  for i in range(0, len(list2)):
    print(list2[i])
  
listvar = loopfuc(list2)


# COMMAND ----------

# DBTITLE 1,Option 4 : Using For Function with Class
class loopcls():
  def loopfuc1(listvar):
    for i in range(0, len(list2)):
      print(list2[i])
  
listvar = loopcls.loopfuc1(list2)


# COMMAND ----------

# DBTITLE 1,Option 5 : Using For Lambda
list(map(lambda y: print(y), list2))