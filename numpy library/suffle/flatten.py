import numpy as np

var = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(var)

print(var.flatten())

# by using flatten in 'F' this convert acroos colume

print(var.flatten(order="F"))

# revel also use like this

print(np.ravel(var))

print(np.ravel(var,order='F'))