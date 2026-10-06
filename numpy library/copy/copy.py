import numpy as np

var = np.array([1,2,3,4,5])

copy_var = np.copy(var)

var[2] = 20

# in copy the changes made in array will only occur in the original array and not in the copy array

print(f"Array : {var}")
print(f"copy: {copy_var}")