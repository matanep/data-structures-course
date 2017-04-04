
### question 1 ###

#Imports
import pandas as pd
import time

#Path for data
path="data1.xlsx"

#Implement Queue class
class Queue():
    def __init__(self,max_size):
        self.max_size= max_size
        self.items = []

    def front(self):
        return self.items[-1]

    def empty(self):
        return self.items == []

    def enqueue(self, item):
        if len(self.items)<self.max_size:
            self.items.insert(0,item)
        else:
            return "Queue is full"

    def dequeue(self):
        return self.items.pop()

#Naive solution (o(n^2))
#Algorithm:
def naive_find_start_country(revenue=[],cost=[]):
    curr_money=0
    for start_country in range(len(revenue)):
        curr_money=0
        for step in range(len(revenue)):
            curr_money=curr_money +revenue[(start_country+step)%len(revenue)] -cost[(start_country+step)%len(revenue)]
            if curr_money <0:
                break
        if curr_money>=0:
            return start_country
    return "No feasible solution"


#solution using Queue (o(n))
#Algorithm
def find_start_country_using_queue(revenue=[],cost=[]):
    queue=Queue(1000)
    curr_money=0
    for step in range(len(revenue)):
        queue.enqueue(step)
        curr_money=curr_money +revenue[step] -cost[step]
        while curr_money<0:
            head=queue.dequeue()
            curr_money=curr_money -revenue[head] +cost[head]
    if queue.empty():
        return "No feasible solution"
    else:
        return queue.dequeue()


#data handling data = pd.ExcelFile(path)
data = pd.ExcelFile(path)
df = data.parse("Sheet1")
revenue=df['revenue'].tolist()
cost=df['cost'].tolist()

#Solving with Naive algorithm:
start_time = time.clock()
print naive_find_start_country(revenue,cost)
print time.clock() - start_time, "seconds"

#solver using queue
start_time = time.clock()
print find_start_country_using_queue(revenue,cost)
print time.clock() - start_time, "seconds"


