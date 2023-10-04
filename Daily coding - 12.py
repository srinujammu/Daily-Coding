# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://blog.devgenius.io/daily-coding-problem-problem-12-8056960a3b61
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# MAGIC
# MAGIC
# MAGIC For example, if N is 4, then there are 5 unique ways:
# MAGIC
# MAGIC
# MAGIC 1, 1, 1, 1
# MAGIC
# MAGIC
# MAGIC 2, 1, 1
# MAGIC
# MAGIC
# MAGIC 1, 2, 1
# MAGIC
# MAGIC
# MAGIC 1, 1, 2
# MAGIC
# MAGIC
# MAGIC 2, 2
# MAGIC
# MAGIC
# MAGIC What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
# MAGIC
# MAGIC
# MAGIC Let’s first focus on the first part of the problem. We are given N steps and we need to find the numbers of unique ways we can climb the staircase.
# MAGIC
# MAGIC
# MAGIC For example if N=1(only one step in the staircase), then we can climb the staircase in possible way.
# MAGIC
# MAGIC
# MAGIC For N=2, we can climb 1-1 steps or 2 steps at a time. So the answer is 2.
# MAGIC
# MAGIC
# MAGIC For N=3, the possible ways are 1–1–1, 1–2 and 2–1. So the answer is 3.
# MAGIC
# MAGIC
# MAGIC N=1, Ways: 1, Total: 1
# MAGIC
# MAGIC
# MAGIC N=2, Ways:1–1; 2, Total:2
# MAGIC
# MAGIC
# MAGIC N=3, Ways:1–1–1; 1–2; 2–1, Total:3
# MAGIC
# MAGIC
# MAGIC N=4, Ways:1–1–1–1; 1–1–2, 1–2–1, 2–1–1; 2–2, Total:5
# MAGIC
# MAGIC
# MAGIC N=5, Ways:1–1–1–1–1; 1–1–1–2; 1–1–2–1; 1–2–1–1; 2–1–1–1; 1–2–2; 2–1–2; 2–2–1, Total:8
# MAGIC
# MAGIC
# MAGIC We can observe a pattern from the above. The number of unique for any given number of steps depends on the previous two answers. For N=4, the answer is 5 which can be written as 3+2 or f(3) + f(2) or f(N-1)+f(N-2).

# COMMAND ----------

def stair(n):
  one, two = 1,1;
  for i in range(n-1):
    temp = one
    one = one+two
    two= temp
  return one

print(stair(11))

# COMMAND ----------

# MAGIC %md
# MAGIC ### It is just a kind of fibbinaci series