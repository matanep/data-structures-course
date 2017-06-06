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

number_of_vertices= max(max(edges))

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

print creat_adjacency_dict(edges)


#part c


#part d

#part e