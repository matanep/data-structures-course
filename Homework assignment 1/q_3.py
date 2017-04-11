
### question 3 ###

#Imports
import pandas as pd

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
            return int(self.m*(key*self.A-int(key*self.A)))

    def hash_function_2(self,key):
        if self.hash_function_method=="mod":
            return (self.m_2-key%self.m_2)
        elif self.hash_function_method=="multiplication":
            return int(self.m_2*(key*self.A_2-int(key*self.A_2)))


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
            if len(self.keys[place])>=1:
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
                new_place=self.hash_function(key+i*self.hash_function_2(key))
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

        elif self.collision_handling == "Chain":
            if self.keys[place] == []:
                counter += 1
                return "Data is not in Hash Table",counter
            if len(self.keys[place]) >= 1:
                counter+=1
                for i in range(1,len(self.keys[place])):
                    counter += 1
                    if self.keys[place][i] == key:
                        del self.keys[i]
                        del self.data[place][i]
                        self.num_keys -= 1
                        return counter
                return "Data is not in Hash Table",counter

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
            return "Data is not in Hash Table",counter

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
            return "Data is not in Hash Table"  ,counter

    def member(self, key=int):
        counter = 0
        place = self.hash_function(key)
        if self.keys[place] == [key]:
            counter += 1
            return True, counter

        elif self.collision_handling == "Chain":
            if self.keys[place] == []:
                counter += 1
                return False, counter
            if len(self.keys[place]) >= 1:
                counter+=1
                for i in range(1,len(self.keys[place])):
                    counter += 1
                    if self.keys[place][i] == key:
                        return True,counter
                return False,counter

        elif self.collision_handling == "OA_Quadratic_Probing":
            counter+=1
            for i in range(1, self.size):
                counter += 1
                new_place = self.hash_function(place + i * i)
                if self.keys[new_place] == [key]:
                    return True,counter
            return False,counter

        elif self.collision_handling == "OA_Double_Hashing":
            counter+=1
            for i in range(1, self.size):
                counter += 1
                new_place = self.hash_function(key) + i * self.hash_function_2(key)
                if self.keys[new_place] == [key]:
                    return True,counter
            return False,counter


#data handling data = pd.ExcelFile(path)
data = pd.ExcelFile(path)
df_1 = data.parse("Sheet1")
keys_1=df_1['ID'].tolist()
data_1=df_1['Name'].tolist()

df_2 = data.parse("Sheet2")
keys_2=df_2['ID'].tolist()
data_2=df_2['Name'].tolist()

df_3 = data.parse("Sheet3")
keys_3=df_3['ID'].tolist()
data_3=df_3['Name'].tolist()

datas_and_keys=[(data_1,keys_1),(data_2,keys_2),(data_3,keys_3)]

for data,keys in datas_and_keys:
    print "***"
    Hash_Table_1=HashTable(149,"mod","Chain",149,0,0,0)
    Hash_Table_2=HashTable(149,"mod","OA_Quadratic_Probing",149,0,0,0)
    Hash_Table_3=HashTable(149,"mod","OA_Double_Hashing",149,0,97,0)
    Hash_Table_4=HashTable(149,"multiplication","Chain",149,0.589,0,0)
    Hash_Table_5=HashTable(149,"multiplication","OA_Quadratic_Probing",149,0.589,0,0)
    Hash_Table_6=HashTable(149,"multiplication","OA_Double_Hashing",149,0.589,97,0.309)
    Hash_Tables=[Hash_Table_1,Hash_Table_2,Hash_Table_3,Hash_Table_4,Hash_Table_5,Hash_Table_6]
    for Hash_Table in Hash_Tables:
        count_in=0
        count_is=0
        for i in range(len(keys_1)):
            moves=Hash_Table.insert(int(keys[i]),value=data[i])
            count_in+=moves
        print count_in



#Todo: raiz error if inpuot parameters are not defined