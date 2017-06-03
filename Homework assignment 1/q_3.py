### question 3 ###

#Imports:
import pandas as pd

#Path for data:
path="data3.xlsx"

#Implement HashTable class:
class HashTable:
    def __init__(self, size=int , hash_function_method=str, collision_handling=str,m=int,A=float,m_2=int,A_2=float): #Initiate all the parameter for the hash table.
        self.hash_function_method=hash_function_method
        self.collision_handling=collision_handling
        self.size = size
        self.keys =[[] for _ in range(size)] #Data structure for keys.
        self.data = [[] for _ in range(size)]#Data structure for values.
        self.m=m
        self.A=A
        self.m_2=m_2
        self.A_2=A_2
        self.num_keys=0
        #Check that all the parameters are given for a specific configuration of the hash table:
        if self.hash_function_method=="multiplication" and self.A ==float:
            raise ValueError('Need to define A')
        if self.collision_handling=="OA_Double_Hashing" and self.m_2 ==int:
            raise ValueError('Need to define m_2')
        if self.collision_handling=="OA_Double_Hashing" and self.hash_function_method=="multiplication" and self.A_2 ==float:
            raise ValueError('Need to define A_2')

    def hash_function(self,key):                #Logic of hash function.
        if self.hash_function_method=="mod":
            return key%self.m
        elif self.hash_function_method=="multiplication":
            return int(self.m*(key*self.A-int(key*self.A)))

    def hash_function_2(self,key):              #Logic of hash function, when using OA_Double_Hashing.
        if self.hash_function_method=="mod":
            return (self.m_2-key%self.m_2)
        elif self.hash_function_method=="multiplication":
            return int(self.m_2*(key*self.A_2-int(key*self.A_2)))


    def insert(self,key=int,value=str):
        counter=0                           #We will use the counter later to create our metric of efficiency.
        place= self.hash_function(key)
        if self.keys[place]==[]:            #If we did not have any collision.
            self.keys[place]=[key]
            self.data[place]=[data]
            counter+=1
            self.num_keys += 1
            return counter
        elif self.keys[place]==[key]:       #Replacing the value.
            self.data[place]=[data]
            counter+=1
            return counter
        #hendeling collisions:
        elif self.collision_handling=="Chain":
            if len(self.keys[place])>=1:
                counter+=1
                for i in range(1,len(self.keys[place])):
                    counter+=1
                    if self.keys[place][i]==key:        #Replacing the value.
                        self.data[place][i]=value
                        self.num_keys += 1
                        return counter                  #Returns the amount of operations.
                self.keys[place].append(key)            #Using 'Chain'.
                self.data[place].append(value)
                self.num_keys += 1
                return counter                          #Returns the amount of operations.

        elif self.collision_handling=="OA_Quadratic_Probing":
            if self.num_keys==self.size:
                return "Hash Table is full"             #In open addressing, we can not have more keys then the size of the data structure.
            counter+=1
            for i in range(1,self.size):
                counter+=1
                new_place=self.hash_function(place +i*i)
                if self.keys[new_place]==[key]:         #Replacing the value.
                    self.data[new_place]=[value]
                    return counter                      #Returns the amount of operations.
                elif self.keys[new_place]==[]:
                    self.keys[new_place]=[key]          #Using 'OA_Quadratic_Probing'.
                    self.data[new_place]=[value]
                    self.num_keys+=1
                    return counter                      #Returns the amount of operations.

        elif self.collision_handling=="OA_Double_Hashing":
            if self.num_keys==self.size:
                return "Hash Table is full"             #In open addressing, we can not have more keys then the size of the data structure.
            counter+=1
            for i in range(1,self.size):
                counter+=1
                new_place=self.hash_function(key+i*self.hash_function_2(key))
                if self.keys[new_place] == [key]:       #Replacing the value.
                    self.data[new_place] = [value]
                    return counter                      #Returns the amount of operations.
                elif self.keys[new_place]==[]:
                    self.keys[new_place]=[key]
                    self.data[new_place]=[value]        #Using 'OA_Double_Hashing'.
                    self.num_keys+=1
                    return counter                      #Returns the amount of operations.

    def delete(self,key=int):
        counter = 0                                     #We will use the counter later to create our metric of efficiency.
        place = self.hash_function(key)
        if self.keys[place] == [key]:
            del self.keys[place]
            del self.data[place]
            counter += 1                                #If we did not have any collision.
            self.num_keys -= 1                          #Update the number of keys in the hash table.
            return counter                              #Returns the amount of operations.

        elif self.collision_handling == "Chain":
            if self.keys[place] == []:
                counter += 1
                return "Data is not in Hash Table",counter  #Data is not in Hash Table, Returns the amount of operations.
            if len(self.keys[place]) >= 1:
                counter+=1
                for i in range(1,len(self.keys[place])):
                    counter += 1
                    if self.keys[place][i] == key:
                        del self.keys[i]                   #Go over all keys in a specific place in the hash table.
                        del self.data[place][i]
                        self.num_keys -= 1                 #Update the number of keys in the hash table.
                        return counter                     #Found and deleted, Returns the amount of operations.
                return "Data is not in Hash Table",counter #Data is not in Hash Table, Returns the amount of operations.

        elif self.collision_handling == "OA_Quadratic_Probing":
            counter+=1
            for i in range(1, self.size):
                counter += 1
                new_place = self.hash_function(place + i * i)
                if self.keys[new_place] == [key]:
                    del self.keys[new_place]
                    del self.data[new_place]                #Go over all places the key can be - using OA Quadratic Probing.
                    self.num_keys -= 1                      #Update the number of keys in the hash table.
                    return counter                          #Found and deleted, Returns the amount of operations.
            return "Data is not in Hash Table",counter      #Data is not in Hash Table, Returns the amount of operations.

        elif self.collision_handling == "OA_Double_Hashing":
            counter+=1
            for i in range(1, self.size):
                counter += 1
                new_place = self.hash_function(key+i*self.hash_function_2(key))
                if self.keys[new_place] == [key]:
                    del self.keys[new_place]                #Go over all places the key can be - using OA Double Hashing.
                    del self.data[new_place]
                    self.num_keys -= 1                      #Update the number of keys in the hash table.
                    return counter                          #Found and deleted, Returns the amount of operations.
            return "Data is not in Hash Table"  ,counter    #Data is not in Hash Table, Returns the amount of operations.

    def member(self, key=int):
        counter = 0                                         #We will use the counter later to create our metric of efficiency.
        place = self.hash_function(key)
        if self.keys[place] == [key]:                       #If we did not have any collision.
            counter += 1
            return True, counter                            #Returns True and the amount of operations.

        elif self.collision_handling == "Chain":
            if self.keys[place] == []:
                counter += 1
                return False, counter                       #Go over all keys in a specific place in the hash table,
            if len(self.keys[place]) >= 1:                  #if the key is in it return True and the amount of operations,
                counter+=1                                  #elsr False and the amount of operations
                for i in range(1,len(self.keys[place])):
                    counter += 1
                    if self.keys[place][i] == key:
                        return True,counter
                return False,counter

        elif self.collision_handling == "OA_Quadratic_Probing":
            counter+=1
            for i in range(1, self.size):
                counter += 1                                    #Go over all places the key can be - using OA Quadratic Probing,
                new_place = self.hash_function(place + i * i)   #if the key is in it return True and the amount of operations,
                if self.keys[new_place] == [key]:               #else False and the amount of operations.
                    return True,counter
            return False,counter

        elif self.collision_handling == "OA_Double_Hashing":
            counter+=1
            for i in range(1, self.size):                                           #Go over all places the key can be - using OA Double Hashing,
                counter += 1                                                        #if the key is in it return True and the amount of operations,
                new_place = self.hash_function(key+i*self.hash_function_2(key))     #else False and the amount of operations.
                if self.keys[new_place] == [key]:
                    return True,counter
            return False,counter


#data handling:
data = pd.ExcelFile(path)   #Import 'Sheet1'.
df_1 = data.parse("Sheet1")
keys_1=df_1['ID'].tolist()
data_1=df_1['Name'].tolist()

df_2 = data.parse("Sheet2") #Import 'Sheet2'.
keys_2=df_2['ID'].tolist()
data_2=df_2['Name'].tolist()

df_3 = data.parse("Sheet3") #Import 'Sheet3'.
keys_3=df_3['ID'].tolist()
data_3=df_3['Name'].tolist()

datas_and_keys=[(data_1,keys_1),(data_2,keys_2),(data_3,keys_3)] #List of namas for all data and kets list.

#Solve question 3:
n=1#The data we are working on now.
for data,keys in datas_and_keys: #Go over each data set.
    print "~~~~Data set",n,':~~~~'
    Hash_Table_1=HashTable(149,"mod","Chain",149,0,0,0)
    Hash_Table_2=HashTable(149,"mod","OA_Quadratic_Probing",149,0,0,0)
    Hash_Table_3=HashTable(149,"mod","OA_Double_Hashing",149,0,97,0)
    Hash_Table_4=HashTable(149,"multiplication","Chain",149,0.589,0,0)
    Hash_Table_5=HashTable(149,"multiplication","OA_Quadratic_Probing",149,0.589,0,0)
    Hash_Table_6=HashTable(149,"multiplication","OA_Double_Hashing",149,0.589,97,0.405)
    Hash_Tables=[Hash_Table_1,Hash_Table_2,Hash_Table_3,Hash_Table_4,Hash_Table_5,Hash_Table_6]
    hn=1#The hash table we are working on now.
    for Hash_Table in Hash_Tables: #Go over each Hash table
        count_in=0
        for i in range(len(keys)):
            moves=Hash_Table.insert(int(keys[i]),value=data[i]) #Inser all data.
            count_in+=moves                                     #Count all the operations.
        print '##Hash Table '+str(hn)+':',float(count_in)/len(keys)
        hn+=1
    n+=1
