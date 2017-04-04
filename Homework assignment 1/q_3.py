
### question 3 ###

#Imports
import pandas as pd
import time

#Path for data
path="data3.xlsx"

#Implement HashTable class
class HashTable:
    def __init__(self, size=int , hash_function_method=str, collision_handling=str,m=int,A=float):
        self.hash_function_method=hash_function_method
        self.collision_handling=collision_handling
        self.size = size
        self.keys =[[] for _ in range(size)]
        self.data = [[] for _ in range(size)]
        self.m=m
        self.A=A


    def hash_function(self,key):
        if self.hash_function_method=="mod":
            return key%self.m
        elif self.hash_function_method=="multiplication":
            return self.m*int(key*self.A-int(key*self.A))

    def member(self,key):
        #todo

    def insert(self,key=int,value=str):
        counter=0
        palce= self.hash_function(key)
        if self.keys[palce]==[]:
            self.keys[palce]=[key]
            self.data[palce]=[data]
            counter+=1
            return counter
        elif self.keys[palce]==[key]:
            self.data[palce]=[data]
            counter+=1
            return counter
        elif self.collision_handling=="Chain":
            if len(self.keys[palce])>1:
                for i in range(len(self.keys[palce])):
                    counter+=1
                    if self.keys[palce][i]==key:
                        self.data[palce][i]=value
                        return counter
                self.keys[palce].append(key)
                self.data[palce].append(value)
                return counter
        elif self.collision_handling==


    def delete(self,key=int):
        #todo

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


