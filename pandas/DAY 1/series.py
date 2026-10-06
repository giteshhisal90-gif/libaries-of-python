import pandas as pd

x = [2,3,4,5,6,7,8,9]

var = pd.Series(x)

print(var)

# when i want get element

print(var[2])

dic = {"name":["gitesh","hissal","c--"],"fan":[2,3,4,5],"arr":[2,5,6,8,9]}
var1 = pd.Series(dic)
print(var1)

# when i want made seies of same data

s = pd.Series(13,index = [1,2,3,4,5,6,7])
print(s)

# when i want to add data

p = pd.Series(12,index=[2,3,4,5])

print(s+p)