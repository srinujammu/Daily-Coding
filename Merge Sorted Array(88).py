# Databricks notebook source
class Solution:
    def merge(self, nums1, m, nums2, n):
        tmp, n, m = m+n-1, n-1, m-1
        while n>=0:
            if m>=0 and nums1[m] > nums2[n]:
                nums1[tmp]=nums1[m]
                m-=1
            else:
                nums1[tmp]= nums2[n]
                n-=1
            tmp-=1
        return nums1


clscall = Solution()
print(clscall.merge([1,2,3,0,0,0],3,[2,5,6],3))

# COMMAND ----------


