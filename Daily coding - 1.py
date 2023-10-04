# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://github.com/offamitkumar/Daily-Coding-Problem

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC This problem was recently asked by Google.
# MAGIC
# MAGIC Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# MAGIC
# MAGIC For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# MAGIC
# MAGIC Bonus: Can you do this in one pass?
# MAGIC
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,Option 1:
k=9;
arry = [1, 3, 5, 6, 8];

flg = False
def sum_k( k, arr):
  for i in range(0,len(arry)):
    for j in range(i+1,len(arry)):
      if (arry[i]+arry[j]== k):
        #print((arry[i]+arry[j])
        return True
  return False
      
fun_call = sum_k(k, arry);
print(fun_call)

# COMMAND ----------

# DBTITLE 1,Option 2:
class add_class():
  
  def add_fun(self, k, arry):
    temp_set = set();
    for num in arry:
      if num in temp_set:
        return True
      temp_set.add(k-num);
    return False
  
init_cls = add_class();
k = 62
arry= [45, 18, 9, 13, 12] 
print(init_cls.add_fun(k,arry))

# COMMAND ----------

class Solution:
    def twoSum(self, nums, target) :
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    
                    return [i,j]
                  
call_cls = Solution()
print(call_cls.twoSum([2,7,11,15], 9))