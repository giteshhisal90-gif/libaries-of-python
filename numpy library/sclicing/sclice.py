import numpy as np

x = np.array([1,2,3,4,5])
print(x)
print(x[1 : 4])  #start : end(n-1) : step
print(x[::2])
print(x[::-1])

var = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(var[1,1:])
print(var[2,0:3])
print(var[0,::-1])