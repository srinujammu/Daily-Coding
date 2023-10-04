# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference :https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
# MAGIC
# MAGIC Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# MAGIC
# MAGIC Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# MAGIC
# MAGIC Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# MAGIC Return k.

# COMMAND ----------

class Solutions :
  def removeElement(self, varlist, varvalue):
    tmp = []
    for i in varlist:
      if i != varvalue:
        tmp.append(i)
      


    return len(tmp)

varSol = Solutions() 
varlist = [3,2,2,3]
varvalue = 3
varSol.removeElement(varlist, varvalue)

# COMMAND ----------


class Solution:
    def removeElement(self, nums, val) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


varSol = Solution() 
varlist = [3,2,2,3]
varvalue = 2
varSol.removeElement(varlist, varvalue)

# COMMAND ----------

