### question 2 ###

#Imports:
import pandas as pd

#Path for data:
path="edges.xlsx"

#Data handling:
data = pd.ExcelFile(path)
df = data.parse("Sheet1")
edges=df.tolist()  #list of the revenues.


print edges