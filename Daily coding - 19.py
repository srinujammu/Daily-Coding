# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
# MAGIC
# MAGIC
# MAGIC You are given an array prices where prices[i] is the price of a given stock on the ith day.
# MAGIC
# MAGIC You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# MAGIC
# MAGIC Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# MAGIC

# COMMAND ----------

class Solution:
    def maxProfit(self, prices) -> int:



        max_var = prices[-1]
        min_var = prices[-1]
        tmp = 0
        print(prices, tmp, max_var, min_var)

        for i in range(-1, -len(prices)-1,-1):
          if prices[i] < min_var :
            min_var = prices[i] 
          if prices[i] > max_var :
            max_var = prices[i]
            print(max_var)
          print(prices[i], min_var)

        return max_var-min_var



callCls = Solution()
print(callCls.maxProfit([7,1,5,3,6,4]))
print(len(set([7,1,5,3,6,4])))

# COMMAND ----------

class Solution:
    def maxProfit(self, prices) -> int:
        if len(set(prices))<2:
            return 0
        maxp = 0
        minp = prices[0]
        for i in range(1, len(prices)):		
            maxp = max(maxp, prices[i] - minp)
            print("maxp",maxp, "i:",prices[i])
            minp = min(minp, prices[i])
            print("minp",minp)
        return maxp
callCls = Solution()
print(callCls.maxProfit([7,1,5,3,6,4]))

      