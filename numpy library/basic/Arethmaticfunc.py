# np.min(x)
# np.max(x)
# np.argmin(x)
# np.sqrt(x)
# np.sin(x)
# np.cos(x)
# np.cumsum(x)
import numpy as np

var = np.array([3,2,1,5,6,7,8])
var1 = np.array([[7,1,3],[4,6,5]])

print(f"min : {np.min(var)} {np.argmin(var)}")
print(f"max : {np.max(var)} {np.argmax(var)}")
print(f"squre root : {np.sqrt(var)}")
print(f"sin value : {np.sin(var)}")
print(f"cos value : {np.cos(var)}")

# axis = 0 work along coloumn
# axis = 1 work along row
print(f"min of 2d : {np.min(var1,axis=0)}")

print(f"cumsum : {np.cumsum(var)}")
