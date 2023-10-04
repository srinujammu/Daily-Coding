# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://blog.devgenius.io/daily-coding-problem-problem-3-5d41600bc5fe
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# MAGIC
# MAGIC Given this implementation of cons:
# MAGIC
# MAGIC def cons(a, b):
# MAGIC
# MAGIC def pair(f):
# MAGIC
# MAGIC return f(a, b)
# MAGIC
# MAGIC
# MAGIC return pair
# MAGIC
# MAGIC Implement car and cdr.
# MAGIC

# COMMAND ----------

# DBTITLE 1,Passing function as an argument in Python
def shout(s):
  return s.upper()

str = "Hello"
print (str)
print(shout(str))

# COMMAND ----------

# DBTITLE 1,Higher Order Functions : Base Example
def upper_fuc(x):
  return x.upper()

def lower_fuc(x):
  return x.lower()

def higer_order_fuc(func_object):
  temp_var = func_object(str)
  return temp_var


str = "Hi, Data Engineer"

call_var = higer_order_fuc(upper_fuc)
print(call_var)

print(higer_order_fuc(lower_fuc))

# COMMAND ----------

# DBTITLE 1,Option 1: using Lambda 
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(x):
    return x(lambda a, b: a)

def cdr(x):
    return x(lambda a, b: b)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))