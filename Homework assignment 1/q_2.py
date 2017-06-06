
### question 2 ###

#Imports:
import pandas as pd
import time

#Path for data:
path="data2.xlsx"

#Implement Stack class:
class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) < self.max_size:  # Check that the length of the stack is less than the 'maximum_size'.
            self.items.append(item)
        else:
            return "Queue is full"

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

#Naive solution (o(n^2)):
#Algorithm:
def naive_get_index(reports=[]):    #For each week check all the weeks prior to it.
    index=[0]                       #Create an empty list for the results.
    for week in range(1,len(reports)):  #Go over each week.
        curr_index=0
        for week_step in reversed(range(week)): #Go over each week prior to the week you check this time.
            if reports[week] >= reports[week_step]:
                curr_index+=1                   #If the number of reportes in this week is greater than the number of reportes
            else:                               #in the week we check now, add one to the current index and check the week before
                break                           #else, end the for loop and add the current index to the index list.
        index.append(curr_index)
    return index                    #Return the index list.


#solution using stack (o(n)):                       #You can find an explanation to this algoritan in the ppt.
#Algorithm:
def get_index_using_stack(reports=[]):
    index=[0]
    stack=Stack(1000)                               #Configure stack.
    stack.push(0)                                   #Pust to stack the first week.
    for week in range(1,len(reports)):              #Go over every week.
        while stack.empty()==False and reports[week] >= reports[stack.top()]:    #As long as the reports in the current week is greater than the number of
            stack.pop()                                                         #reports in the top of the stack, pop the last week from the stack.
        if stack.empty():
            index.append(week)                                                  #If the stack is empty, append the current week to the index list.
        else:
            index.append(week-stack.top()-1)                                    #Else, add to index list this calculation: (week-week_in_the_top_of_stack -1).
        stack.push(week)
    return index                    #Return the index list.

#Data handling:
data = pd.ExcelFile(path)
df = data.parse("Sheet1")
neighborhoods=list(df)[1:] #Crate the list of neighborhoods in the data.
if len(neighborhoods[0])==0: #Handling no data.
    raise ValueError('No data')


#Solving with Naive algorithm:
start_time = time.clock()
print "##Solving using naive algorithm##"
index=[]
for neighborhood in neighborhoods:      #Go over every neighborhood and add solution to list
    n_index=naive_get_index(df[neighborhood])
    index.append(n_index)
print 'Neighborhoods index is: ',index
print "Time to solution: ",time.clock() - start_time, "seconds"

#Solver using queue:
start_time = time.clock()
print "\n##Solving using stack##"
index=[]
for neighborhood in neighborhoods:      #Go over every neighborhood and add solution to list
    n_index=get_index_using_stack(df[neighborhood])
    index.append(n_index)
print 'Neighborhoods index is: ',index
print "Time to solution: ",time.clock() - start_time, "seconds"
