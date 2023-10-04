# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://blog.devgenius.io/daily-coding-problem-problem-7-d2dc3bbf7c30
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Given the mapping a = 1, b = 2, … z = 26, and an encoded message, count the number of ways it can be decoded.
# MAGIC
# MAGIC For example, the message ‘111’ would give 3, since it could be decoded as ‘aaa’, ‘ka’, and ‘ak’.
# MAGIC
# MAGIC You can assume that the messages are decodable. For example, ‘001’ is not allowed.
# MAGIC
# MAGIC Hint: It is similar to Fibonacci series

# COMMAND ----------

str = "65"
print(chr(len(str))) 

#ASCII Conversion : 65 to 90

print (ord("A"))

123

A B C KC AX

45678
DEFGH    




# COMMAND ----------

import time
def count_decoding(digits: str):
    len_digits = len(digits)
    
    # dynamic Programming table
    count = [0 for _ in range(len_digits + 1)]
    print("inital values :", count)
    
    # base cases
    count[0] = 1
    count[1] = 1
    print("Before loop (Count): " , count)
    print("--------------------------------------")
    for i in range(2, len_digits + 1):
        print("--------------------------------------")
        time.sleep(3)
        print("First count in loop : " , count)
        count[i] = 0
        # if the last digit is not 0, then last digit must add to the number of words
        print ("Before IF digit[i-1] value > 0" ,digits[i-1], digits[i - 1] > "0")
        if digits[i - 1] > "0":
            count[i] = count[i - 1]
            print("count[i] :" , count[i],'\n', "digits[i-1] : ", digits[i-1] ,'\n', count)
        # if the number formed by the last 2 digits is less than 26, its a valid
        # character
        print ("Before 2nd IF digits[i - 2] == 1 or (digits[i - 2] == 2 and digits[i - 1] < 7" ,digits[i - 2] == "1" or (digits[i - 2] == "2" and digits[i - 1] < "7"), "digits[i - 2] : " ,digits[i - 2], "digits[i - 1] : " ,digits[i - 1])
        if digits[i - 2] == "1" or (digits[i - 2] == "2" and digits[i - 1] < "7"):
            #print(count[i], i,  digits[i] , digits[i - 1],  digits[i - 2] )
            count[i] += count[i - 2]
            print(count[i], count[i-2],  count)
    print(" ----------------------------------------------- ")
    print("Final  Count : " , count)
    return count[len_digits]


if __name__ == "__main__":
    print(count_decoding("12255"))
    #print(count_decoding("11"))
   # print(count_decoding("111"))
   # print(count_decoding("1311"))
   # print(count_decoding("1111"))
