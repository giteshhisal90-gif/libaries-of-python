import numpy as np

arr =np.array([1,2,3,4,5]) 
print(arr)
print(type(arr))
print(arr.ndim)

l =[]
for i in range(5):
    num = int(input("Enter a numbe : "))
    l.append(num)

arr = np.array(l)
print(arr)

# x= np.array([1,2,3,4,5])  #one dimentional
# print(x)
# print(x.ndim)

# y = np.array([[1,2,3,4],[2,3,4,5]])
# print(y)
# print(y.ndim)

# z= np.array([[[1,2,3],[1,2,3],[1,2,3]]])
# print(z)
# print(z.ndim)
