
### question 3 ###

#Imports
import pandas as pd
import time

#Path for data
path="data3.xlsx"

#Implement HashTable class
class HashTable:
    def __init__(self, size=int , hash_function_method=str, collision_handling=str,m=int,A=float,m_2=0,A_2=0.0):
        self.hash_function_method=hash_function_method
        self.collision_handling=collision_handling
        self.size = size
        self.keys =[[] for _ in range(size)]
        self.data = [[] for _ in range(size)]
        self.m=m
        self.A=A
        self.m_2=m_2
        self.A_2=A_2
        self.num_keys=0


    def hash_function(self,key):
        if self.hash_function_method=="mod":
            return key%self.m
        elif self.hash_function_method=="multiplication":
            return self.m*int(key*self.A-int(key*self.A))

    def hash_function_2(self,key):
        if self.hash_function_method=="mod":
            return key%self.m_2
        elif self.hash_function_method=="multiplication":
            return self.m_2*int(key*self.A_2-int(key*self.A_2))


    def insert(self,key=int,value=str):
        counter=0
        place= self.hash_function(key)
        if self.keys[place]==[]:
            self.keys[place]=[key]
            self.data[place]=[data]
            counter+=1
            self.num_keys += 1
            return counter
        elif self.keys[place]==[key]:
            self.data[place]=[data]
            counter+=1
            return counter

        elif self.collision_handling=="Chain":
            if len(self.keys[place])>1:
                counter+=1
                for i in range(1,len(self.keys[place])):
                    counter+=1
                    if self.keys[place][i]==key:
                        self.data[place][i]=value
                        self.num_keys += 1
                        return counter
                self.keys[place].append(key)
                self.data[place].append(value)
                self.num_keys += 1
                return counter

        elif self.collision_handling=="OA_Quadratic_Probing":
            if self.num_keys==self.size:
                return "Hash Table is full"
            counter+=1
            for i in range(1,self.size):
                counter+=1
                new_place=self.hash_function(place +i*i)
                if self.keys[new_place]==[key]:
                    self.data[new_place]=[value]
                    return counter
                elif self.keys[new_place]==[]:
                    self.keys[new_place]=[key]
                    self.data[new_place]=[value]
                    self.num_keys+=1
                    return counter

        elif self.collision_handling=="OA_Double_Hashing":
            if self.num_keys==self.size:
                return "Hash Table is full"
            counter+=1
            for i in range(1,self.size):
                counter+=1
                new_place=self.hash_function(key)+i*self.hash_function_2(key)
                if self.keys[new_place] == [key]:
                    self.data[new_place] = [value]
                    return counter
                elif self.keys[new_place]==[]:
                    self.keys[new_place]=[key]
                    self.data[new_place]=[value]
                    self.num_keys+=1
                    return counter




    def delete(self,key=int):
        counter = 0
        place = self.hash_function(key)
        if self.keys[place] == [key]:
            del self.keys[place]
            del self.data[place]
            counter += 1
            self.num_keys -= 1
            return counter
        #########################################del when is empty

        elif self.collision_handling == "Chain":
            if self.keys[place] == []:
                counter += 1
                return "Data is not in Hash Table"
            if len(self.keys[place]) > 1:
                counter+=1
                for i in range(1,len(self.keys[place])):
                    counter += 1
                    if self.keys[place][i] == key:
                        del self.keys[i]
                        del self.data[place][i]
                        self.num_keys -= 1
                        return counter
                return "Data is not in Hash Table"

        elif self.collision_handling == "OA_Quadratic_Probing":
            counter+=1
            for i in range(1, self.size):
                counter += 1
                new_place = self.hash_function(place + i * i)
                if self.keys[new_place] == [key]:
                    del self.keys[new_place]
                    del self.data[new_place]
                    self.num_keys -= 1
                    return counter
            return "Data is not in Hash Table"

        elif self.collision_handling == "OA_Double_Hashing":
            counter+=1
            for i in range(1, self.size):
                counter += 1
                new_place = self.hash_function(key) + i * self.hash_function_2(key)
                if self.keys[new_place] == [key]:
                    del self.keys[new_place]
                    del self.data[new_place]
                    self.num_keys -= 1
                    return counter
            return "Data is not in Hash Table"

    def member(self, key):
        # todo

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


