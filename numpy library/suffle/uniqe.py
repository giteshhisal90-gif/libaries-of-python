import numpy as np

var = np.array([5,2,3,4,5,1,6,2,3,4,8,9,6])

print(var)

x = np.unique(var, return_index=True,return_counts=True)
print(x)
