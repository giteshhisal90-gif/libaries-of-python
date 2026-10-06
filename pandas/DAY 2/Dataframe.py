import pandas as pd

l=[1,2,3,4,5,6,7]

var = pd.DataFrame(l)

print(var)

# we can pass dictionary
d = {"a": [1,2,3,4,5,6],"b":[12,13,15,17,19,14],"c":['A','B','C','D','E','F']}

var1 = pd.DataFrame(d)

# we can selec coloum to display
# var2 = pd.DataFrame(d,columns=["a","b"])

print(var1)
# print(var2)
# we can asses data 
print(var1['a'][2])

# instead of dictionary when we get data from a list of list then it 
# it consider each list of list as a row

list_1 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
variable = pd.DataFrame(list_1)
print(variable)