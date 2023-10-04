# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
# MAGIC
# MAGIC 1768. Merge Strings Alternately
# MAGIC
# MAGIC You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# MAGIC
# MAGIC Return the merged string.
# MAGIC

# COMMAND ----------

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = ""
        temp1 = max(len(word1),len(word2))
        
        for i in range(0,temp1):
          if(i < len(word1)):
            temp = temp+word1[i]
            #temp =+word1[i]
                #temp.append(self.word1[i])
          if (i < len(word2)):
            
            temp = temp+word2[i]
            #temp =+word2[i]
                #temp.append(self.word
        return temp
     

      

varClas = Solution();
print(varClas.mergeAlternately("abcz","cdF"));
