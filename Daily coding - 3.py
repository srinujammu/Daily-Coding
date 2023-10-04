# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://github.com/offamitkumar/Daily-Coding-Problem

# COMMAND ----------

# MAGIC %md
# MAGIC This problem was asked by Google.
# MAGIC
# MAGIC Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# MAGIC
# MAGIC For example, given the following Node class
# MAGIC
# MAGIC class Node:
# MAGIC   
# MAGIC def __init__(self, val, left=None, right=None):
# MAGIC   
# MAGIC   
# MAGIC      self.val = val
# MAGIC     
# MAGIC      self.left = left
# MAGIC       
# MAGIC      self.right = right
# MAGIC     
# MAGIC The following test should be passed
# MAGIC
# MAGIC node = Node('root', Node('left', Node('left.left')), Node('right'))
# MAGIC
# MAGIC assert deserialize(serialize(node)).left.left.val == 'left.left'
# MAGIC
# MAGIC Hint : 
# MAGIC
# MAGIC https://leetcode.com/problems/serialize-and-deserialize-bst/
# MAGIC
# MAGIC https://github.com/offamitkumar/Daily-Coding-Problem/blob/master/Solution/Day-003.cpp
# MAGIC

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