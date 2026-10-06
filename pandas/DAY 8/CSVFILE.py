import pandas as pd

csv = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv")


print(csv)
print(csv.columns)
print(csv.index)
print(csv.describe())

print(csv.head(3))
print(csv.tail(3))

print(csv[:6])

print(csv.index.array)

print(csv.to_numpy())

import numpy as np 

v = np.asarray(csv)
print(v)

print(csv.sort_index(axis = 0 ,ascending = False))
# axis 0 means work along the rows and axis 1 means work along the columns


# to change the value of a particular cell in the csv file we can use loc method
csv.loc[0,'A'] = 100
print(csv)


print(csv.loc[[2,3],['A','B']])


# when we want to remove ani colum or row we use drop()

print(csv.drop('A',axis = 1)) # axis 1 means column and axis 0 means row
