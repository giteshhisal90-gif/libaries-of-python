import  pandas as pd

data = pd.DataFrame({" name":['A','B','A','C','B','C','A','B','C'],
                     "score":[1,2,3,4,5,6,7,8,9],"subject":['Math','Math','English','English','Math','English','Math','English','Math']})


datag=data.groupby(' name')
for name,group in datag:
    print(name)
    print(group)
    print("***************")


print(datag.get_group('A'))
print(datag.min())
print(datag.max())
# print(datag.mean())
li = list(datag)
print(li)