# Databricks notebook source
# MAGIC %md
# MAGIC Problem 579
# MAGIC
# MAGIC This problem was asked by Flipkart.
# MAGIC
# MAGIC Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.
# MAGIC
# MAGIC On the ith jump, you may move exactly i places to the left or right.
# MAGIC
# MAGIC Find a path with the fewest number of jumps required to get from 0 to N.
# MAGIC
# MAGIC Click here(https://github.com/offamitkumar/Daily-Coding-Problem/blob/master/Solution/Day-579.cpp) for solution.

# COMMAND ----------

current = 0;
moves = 0 ;
inc = 1;
target = 3

# COMMAND ----------

while True:
  
  if target == current:
    break;
  if target < current and (target-current)%2 == 0:
    break;
  current = inc;
  inc = inc+1;
  moves = moves+1;
print(moves)

