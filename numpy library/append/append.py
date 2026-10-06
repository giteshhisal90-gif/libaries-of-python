import numpy as np

var = ([1,2,3,4,5,6])
print(var)

# append function can add a float value but in last
x = np.append(var , 6.5)
print(x)

# for 2d

var1 = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(var1)
print()


v = np.append(var1, [[11,12,13,14,15]],axis=0)
print(v)

# when i want to delet a data

arr = np.array([1,2,3,4,5])
print(arr)

s = np.delete(arr, 2) #this remove elent at 2nd index
print(s)