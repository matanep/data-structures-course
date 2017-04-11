
### question 1 ###

#Imports:
import pandas as pd
import time

#Path for data:
path="data1.xlsx"

#Implement Queue class:
class Queue():
    def __init__(self,max_size):
        self.max_size= max_size
        self.items = []

    def front(self):
        return self.items[-1]

    def empty(self):
        return self.items == []

    def enqueue(self, item):
        if len(self.items)<self.max_size:        #Check that the length of the queue is less than the 'maximum_size'.
            self.items.insert(0,item)
        else:
            return "Queue is full"

    def dequeue(self):
        return self.items.pop()

#Naive solution (o(n^2)):                         #Try to start from each country, if you go over all countries - you succeed.
#Algorithm:
def naive_find_start_country(revenue=[],cost=[]): #Gets a list of revenues and a list of costs for each country.
    curr_money=0
    for start_country in range(len(revenue)):
        curr_money=0
        for step in range(len(revenue)):          #Go over all countries.
            curr_money=curr_money +revenue[(start_country+step)%len(revenue)] -cost[(start_country+step)%len(revenue)] #Use% (mod) to create a loop.
            if curr_money <0:
                break               #This route is irrelevant so there is no reason to continue.
        if curr_money>=0:
            return start_country    #Starting from this country workes.
    return "No feasible solution"   #No feasible solution.


#solution using Queue (o(n)):                   #You can find an explanation to this algoritan in the ppt.
#Algorithm:
def find_start_country_using_queue(revenue=[],cost=[]):
    queue=Queue(1000)                           #Configure queue.
    curr_money=0                                #Configure curr_money=0.
    for step in range(len(revenue)):            #Go over all countries.
        queue.enqueue(step)                     #Insert to queue the current country.
        curr_money=curr_money +revenue[step] -cost[step]        #Update the curr_money.
        while curr_money<0:                                     #As long as the curr_money in less than 0 - dequeue,
            head=queue.dequeue()                                #and update the curr_money with the country you dequeued.
            curr_money=curr_money -revenue[head] +cost[head]
    if queue.empty():
        return "No feasible solution"                           #If the queue is empty after you went over all countries - there is no feasible solution,
    else:                                                       #if not, the country in the head of the queue, is the country to start from.
        return queue.dequeue()


#Data handling:
data = pd.ExcelFile(path)
df = data.parse("Sheet1")
revenue=df['revenue'].tolist()  #list of the revenues.
cost=df['cost'].tolist()        #list of the costs.

#Solving with Naive algorithm:
start_time = time.clock()
print "##Solving with Naive algorithm##"
print "Strat from: ",naive_find_start_country(revenue,cost)
print "Time to solution: ", time.clock() - start_time, "seconds"

#Solving using queue:
start_time = time.clock()
print "\n##Solving using queue##"
print "Strat from: ",find_start_country_using_queue(revenue,cost)
print "Time to solution: ",time.clock() - start_time, "seconds"


