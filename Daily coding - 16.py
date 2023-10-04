# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference :https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
# MAGIC
# MAGIC Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# MAGIC
# MAGIC Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# MAGIC
# MAGIC Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# MAGIC Return k.

# COMMAND ----------

class solution:
  def removeDuplicates (self, nums)-> int:
    numtmp = []
    k = 0
    for i in nums:
      if i not in numtmp:
        numtmp.append(i)
        k+=1

    nums=numtmp
        
    return k


num = [1,1,2]
callClass = solution()
callClass.removeDuplicates(num)

# COMMAND ----------

class solution():
    def removeDuplicates(self, nums):
        replace = 1
        for i in range(1, len(nums)):
          print(nums, nums[i], nums[i-1])
          if nums[i-1] != nums[i]:
            print("IF",nums, nums[i], nums[i-1])
            nums[replace] = nums[i]
            replace += 1
        print(nums)
        return replace
      

num = [1,1,2]
callClass = solution()
callClass.removeDuplicates(num)