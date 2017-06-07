### question 2 ###

#Imports:
import pandas as pd
import numpy as np

#Path for data:
path="edges.xlsx"

#Data handling:
data = pd.ExcelFile(path)
df = data.parse("Sheet1")
edges=[tuple(x) for x in df.to_records(index=False)]


# for i in edges:
#     edges.remove((i[1],i[0]))
#
#
# # print len(edges)
# df=pd.DataFrame.from_records(edges)
#
# # print df
# #
# writer = pd.ExcelWriter('edges.xlsx')
# df.to_excel(writer,'Sheet2')
# writer.save()

#part a
def creat_adjacency_matrix(edges=list):
    number_of_vertices = max(max(edges))
    matrix=np.zeros((number_of_vertices,number_of_vertices))
    for edge in edges:
        print edge
        matrix[edge[0]-1,edge[1]-1]=1
        matrix[edge[1]-1, edge[0]-1] = 1
    return matrix

#part b
def creat_adjacency_dict(edges=list):
    adjacency_dict={}
    for edge in edges:
        if edge[0] in adjacency_dict:
            adjacency_dict[edge[0]].append(edge[1])
        else:
            adjacency_dict[edge[0]]=[edge[1]]

        if edge[1] in adjacency_dict:
            adjacency_dict[edge[1]].append(edge[0])
        else:
            adjacency_dict[edge[1]]=[edge[0]]
    return adjacency_dict

print creat_adjacency_dict(edges)[1]


#part c
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

def BFS(edges=list,v=int):
    number_of_vertices = max(max(edges))
    queue=Queue(number_of_vertices)
    visited=[False for i in range(number_of_vertices)]
    print(v)
    visited[v-1]= True
    queue.enqueue(v)
    adjacency_dict=creat_adjacency_dict(edges)
    while (not queue.empty()):
        x= queue.dequeue()
        neighbors_of_x=adjacency_dict[x]
        for neighbor in neighbors_of_x:
            print neighbor
            if not visited[neighbor-1]:
                print neighbor
                visited[neighbor-1]=True
                queue.enqueue(neighbor)

print BFS(edges,1)

#part d