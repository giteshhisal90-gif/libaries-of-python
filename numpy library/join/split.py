import numpy as np 
var = np.array([1,2,3,4,5,6])
print(f"Original array : {var}")

var_split = np.array_split(var,3)
print(f"Split arrays : {var_split}")

print(var_split[0])
print(var_split[0][0])

# spliting array across the y axis
var_split1 = np.split(var,3,axis=0)
print(f"Split arrays y axis: {var_split1}")

# spliting array across the x axis
var1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
var_split2 = np.split(var1,3,axis=1)
print(f"Split arrays x axis: {var_split2}")

# similar to the stack function we have hsplit, vsplit and dsplit functions for spliting array across the x,y and z axis respectively
var_split3 = np.hsplit(var1,3)
print(f"Split arrays h axis: {var_split3}")
var_split4 = np.vsplit(var1,3)
print(f"Split arrays v axis: {var_split4}")
# var_split5 = np.dsplit(var1,3)
# print(f"Split arrays d axis: {var_split5}")

# dsplit function is used for 3D array so it will give error if we use it for 2D array like var1