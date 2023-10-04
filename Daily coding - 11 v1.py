# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://sathishbabu96n.medium.com/daily-coding-problem-problem-10-da50b93bfc67
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# MAGIC
# MAGIC
# MAGIC For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# MAGIC
# MAGIC
# MAGIC Hint: Try pre-processing the dictionary into a more efficient data structure to speed up queries.
# MAGIC
# MAGIC
# MAGIC This is relatively an easy problem which can be solved using regex. Let’s try out with regex!.

# COMMAND ----------

# DBTITLE 1,Basic
import re

str = "The python testing with search words"

x = re.search( "python", str)

if x:
  print(True)
else:
  print(False)

# COMMAND ----------

# DBTITLE 1,level1
import re



def solSearch(s:str, query: list(str)) -> list[str]:
  
  pattern = re.compile(s)
  lst =[]
  for x in query:
    
    r = re.match(pattern, x)
    if r:
      
      lst.append(r.string)
  return lst
      


print(solSearch("de", ["dog", "deer", "deal"]))



# COMMAND ----------

import re
from typing import List


def solution(s: str, query: List[str]) -> List[str]:
    pattern = re.compile(s)
    res = []
    for q in query:
        r = re.match(pattern, q)
        if r:
            res.append(r.string)
    return res
  
  
print(solution("de",["dog", "deer", "deal"]))

# COMMAND ----------

# DBTITLE 1,Compile Functions is special function
# Assign a value to a variable in the code string 
codeString = 'a = 3\nb = 4\nmySum = a + b'
codeObject = compile(codeString, 'add', 'exec')
exec(codeObject)
# We can now use the variables a, b, and mySum
print(f'{a} + {b} = {mySum}')

# COMMAND ----------

# DBTITLE 1,Compile Functions is special function 2
n= 31.006
CubeRoot = "CubeRootFunc = n ** (1./3)"

CubeRootComp = compile(CubeRoot, 'CubeRootFunc', 'exec')

exec(CubeRootComp)

print(f'The cube root of {n} is {CubeRootFunc}')