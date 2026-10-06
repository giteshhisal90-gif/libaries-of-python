import numpy as np
var = np.array([1,2,3,4,5,6])
print(var)
for i in var :
    print(i)

var2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(var2)
print() 
# for assesing element  in lists
for i in var2 :
    print(i)

for i in var2 :
    for j in i :
        print(j)



var3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,22,33]]])
print(var3)
print()
for i in var3 :
    print(i)

for i in var3 :
    for j in i:
        print(j)

for i in var3:
    for j in  i :
        for k in j:
            print(k)


# instead of using for loop we can use function like np.nditer() to iterate through the array
variable = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,22,33]]])
print(variable)
for i in np.nditer(variable):
    print(i)


# we can convert it into buffred
for i in np.nditer(variable ,flags=['buffered'],op_dtypes=['S']):
    print(i)

# for indexing as well as data
for i ,d in np.ndenumerate(variable):
    print(i ,d)