import numpy as np

var = np.array([1,2,3,4])
print(var)


#  variable , positions,value
v = np.insert(var,2,40)
print(v)


# this not accept float value
# when i want to insert a data in two different position

s= np.insert(var , (1,3) , 6)
print(s)

# about 2d array
arr = np.array([[1,2,3],[4,5,6]])

print(arr)
print()


# axis 0 means work along row
arr_new = np.insert(arr,2,6,axis=0)
print(arr_new)
print()

# axis 1 mean work along coloum
arr_new1= np.insert(arr,2,6,axis=1)
print(arr_new1)
print()

# we can add multiple element
arr_new2 = np.insert(arr,2,[9,8,7],axis=0)
print(arr_new2)

