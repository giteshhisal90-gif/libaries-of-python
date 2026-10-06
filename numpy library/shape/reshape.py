import numpy as np

var = np.array([1,2,3,4,5,6,7,8,9])
z = var.reshape(3,3)
print(z)


var2 = np.array([1,2,3,4,5,6,7,8,9,0,1,2])
x = var2.reshape(2,3,2)
print(x)

var3 = np.array([1,2,3,4,5,6,7,8,9,0,1,2])
b = var3.reshape(2,3,2)
print(b)
n = b.reshape(-1)
print(n)
print(n.ndim)
