
### question 3 ###

#Imports
import pandas as pd
import time

#Path for data
path="data3.xlsx"

#Implement Stack class
class Hash_Table:
     def __init__(self,max_size):
         self.max_size= max_size
         self.items = []

     def empty(self):
         return self.items == []

     def push(self, item):
        if len(self.items)<self.max_size:
            self.items.append(item)
        else:
            return "Queue is full"

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]

#Naive solution (o(n^2))
#Algorithm:
def naive_get_index(reports=[]):
    index=[0]
    for week in range(1,len(reports)):
        curr_index=0
        for week_step in reversed(range(week)):
            if reports[week] > reports[week_step]:
                curr_index+=1
            else:
                break
        index.append(curr_index)
    return index


#todo: solution using stack (o(n))
#Algorithm
def get_index_using_stack(reports=[]):
    index=[0]
    stack=Stack(1000)
    stack.push(0)
    for week in range(1,len(reports)):
        while stack.empty()==False and reports[week] > reports[stack.top()]:
            stack.pop()
        if stack.empty():
            index.append(week)
        else:
            index.append(week-stack.top()-1)
        stack.push(week)
    return index

#data handling data = pd.ExcelFile(path)
data = pd.ExcelFile(path)
df = data.parse("Sheet1")
case=df['Azorei Hen'].tolist()

#Solving with Naive algorithm:
start_time = time.clock()
a= naive_get_index(case)
print time.clock() - start_time, "seconds"

#todo: solver using queue
start_time = time.clock()
print max(get_index_using_stack(case))
print time.clock() - start_time, "seconds"


