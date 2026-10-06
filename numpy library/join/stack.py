import numpy as np

var = np.array([1,2,3,4])
var_1 = np.array([5,6,7,8])

# joining two array along the y axis
new_arr = np.stack((var,var_1),axis=0)
print(new_arr)

# joining two array along the x axis
new_arr0 = np.stack((var,var_1),axis=1)
print(new_arr0)

print()
print()
print()

new_arr1= np.hstack((var,var_1))  # row wise stacking
new_arr2 = np.vstack((var,var_1))  # coloumn wise stacking
new_arr3 = np.dstack((var,var_1))  # depth wise stacking
print(new_arr1)
print()
print(new_arr2)
print()
print(new_arr3)