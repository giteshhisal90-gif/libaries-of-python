import numpy as np

var = np.array([1,2,3,4,5,6,7])

var_view = var.view()

var[3] =30

# changes made in array will occur in both original array and view array


print(f"Array : {var}")
print(f"var_view : {var_view}")