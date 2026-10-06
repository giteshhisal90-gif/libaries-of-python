import numpy as np

var = np.array([1,2,3,4])

var1 = np.array([5,6,7,8])

print(f"joined array : {np.concatenate((var,var1))}")