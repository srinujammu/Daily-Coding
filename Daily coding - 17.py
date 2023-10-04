# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# MAGIC
# MAGIC Remove Duplicates from Sorted Array II
# MAGIC
# MAGIC
# MAGIC Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# MAGIC
# MAGIC Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# MAGIC
# MAGIC Return k after placing the final result in the first k slots of nums.
# MAGIC
# MAGIC Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
# MAGIC
# MAGIC Input: nums = [1,1,1,2,2,3]
# MAGIC
# MAGIC Output: 5, nums = [1,1,2,2,3,_]
# MAGIC
# MAGIC Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# MAGIC
# MAGIC It does not matter what you leave beyond the returned k (hence they are underscores).

# COMMAND ----------

print(range(len( [1,1,1,2,2,3])-2,0,-1))

# COMMAND ----------

class solution :
  def removeDuplicates(self, nums) -> int:
    for i in range (len(nums)-2,0,-1):
      if nums[i-1]==nums[i] and nums[i+1]==nums[i]:
        nums.pop(i+1)
    return len(nums)
  
clsObj = solution()
clsObj.removeDuplicates([1,1,1,2,2,3])

