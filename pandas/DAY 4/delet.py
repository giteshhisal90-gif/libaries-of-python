import pandas as pd
var = pd.DataFrame({'A':[1,2,3,4] ,'B':[2,3,4,5],'C':[1,2,3,4]})
print(var)
var.pop('A')

print(var)

del var['B']


print(var)