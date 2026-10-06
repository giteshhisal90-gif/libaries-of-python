import pandas as pd 
var = pd.DataFrame({"A":[1,2,3,4,5],"B":[2,3,4,5,6]})
# data should be equal length
var.insert(2,"New",var["A"]*var["B"])

print(var)


var1 = pd.DataFrame({'A':[1,2,3,4,5],'B':[2,3,4,5,6]})
var1['new_col'] = var1['A'][:3]
print(var1)