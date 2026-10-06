import numpy as np

# adition of 1d
a1 = np.array([1,2,3,4])
print(a1)
new_a1 = a1 + 3 
print(new_a1)

# addition by function
arr = np.array([1,2,3,4])
print(arr)
print(np.add(arr,3))

# adition of 2D
arry = np.array([[1,2,3,4],[1,2,3,4]])
arr1 = np.array([[1,2,3,4],[1,2,3,4]])
print(arry)
print("")
print(arr1)
print("")
print(np.add(arry,arr1))

# subtraction
arry = np.array([[1,2,3,4],[1,2,3,4]])
print(np.subtract(arry,3))

# we can use all these function to perform Arithmetic operation
np.multiply(arry,3)             # *
np.divide(arry,2)               # /
print(np.reciprocal(arr1))      # 1/a
print(np.mod(arr,2))            # %
np.power(arr,2)                 # **