import numpy as np

var = np.array([[1,2,3],[4,5,6]])
var1 = np.array([[7,8,9],[10,11,12]])


# joining two array along the y axis
new_var = np.concatenate((var,var1),axis=0)

# joining two array along the x axis
new_var1 = np.concatenate((var,var1),axis=1)


print(new_var)
print()
print()
print(new_var1)