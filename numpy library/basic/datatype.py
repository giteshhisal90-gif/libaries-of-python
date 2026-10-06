import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8])
# print(f"data type : {arr.dtype}")

# arr1 = np.array([0.1,0.3,0.13,12.20])
# print(f"data type : {arr1.dtype}")

# arr2 = np.array(["s","d","f","g","h"])
# print(f"data type : {arr2.dtype}")

# combination of string and integer

arr3 = np.array(["s","d","f","g","h",1,2,3,4,5])
print(f"data type : {arr3.dtype}")

# when i want to change data type
arr4 = np.array([1,2,3,4,5,6,7,8],dtype=np.int8)
print(f"data type : {arr4.dtype}")

arr5 = np.array([1,2,3,4,5,6,7,8],dtype= "f")
print(f"data type : {arr5.dtype}")


# when i want to use dta rype as a function
arr6 = np.array([1,2,3,4,5,6,7,8])
new = np.float32(arr6)

print(f"data type : {arr6.dtype}")
print(f"data type : {new.dtype}")

print(arr6)
print(new)

# when i want to convert data type directly

x = np.array([1,2,3,4,5,6])
new_1 = x.astype(float)

print(f"data type : {x.dtype}")
print(f"data type : {new_1.dtype}")

print(x)
print(new_1)

