# Databricks notebook source
# DBTITLE 1,Import Libraries
# MAGIC %md
# MAGIC Reference : https://blog.devgenius.io/daily-coding-problem-problem-11-3452b3a63ddb
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

# COMMAND ----------

# DBTITLE 1,*args (Non-Keyword Arguments)
def add(*args):
  list1 = sum(list(map(lambda v : v**2 , args )))
  return list1

#l2 = list(map(lambda v: v ** 2, l1))
add(2,3,5)
  

# COMMAND ----------

# DBTITLE 1,*kwargs (Keyword Arguments)
def kwar(**kwargs):
  
  for key, value in kwargs.items():
        print("%s == %s" % (key, value))
  
dict = {"test":1, "test2":2 , "test3": 3}
kwar(**dict)

# COMMAND ----------

# DBTITLE 1,Simple
import time
def func(**args):
  for i in args:
    print(i)
    sleep(10)
    
l1 = {"job1":2,"job2" : 5,"Job3": 6, "Job4" : 9}
func(**l1)

# COMMAND ----------

from time import sleep, time
class Scheduler:
    def __init__(self):
        self.functions = []
        thread = threading.Thread(target=self._poll)
        thread.start()
    def _poll(self):
        while True:
            now = time() * 1000
            if len(self.functions) > 0:
                due, func, args, kwargs = self.functions[0]
                if now > due:
                    func(*args, **kwargs)
                self.functions = [(due, func, args, kwargs) for due, func, args, kwargs in self.functions if due < now]
            sleep(0.01)
    def schedule(self, func, n, *args, **kwargs):
        heapq.heappush(self.functions, (n + time() * 1000, func, args, kwargs))