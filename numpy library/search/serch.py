import numpy as np

# var = np.array([1,2,3,3,2,6,7,2,8,])

# x = np.where(var == 2)

# print(x)

# # index number of those number which are divisible by 3

# y = np.where((var%3) == 0)
# print(y)

# when i wanna to find position of sutable position of number which i have to insert in the array

var1 = np.array([1,2,3,4,6,7])
poss = np.searchsorted(var1,[5,6,7],side='left')
print(poss)

var1[poss] = [5,6,7]
print(var1)