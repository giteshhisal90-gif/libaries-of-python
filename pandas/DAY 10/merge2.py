import pandas as pd

df1 = pd.DataFrame({
    'A':[1,2,3,4,5],'B':[11,12,13,14,15]})

df2 = pd.DataFrame({
    'A':[1,2,3,4,5],'B':[21,22,23,24,25]})

merge = pd.merge(df1,df2,left_index = True,right_index = True,suffixes = ('name','python'))
print(merge)