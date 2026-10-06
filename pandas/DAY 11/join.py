import pandas as pd 

df1 = pd.DataFrame({'A':[22,44,66,88],'B':[43,54,76,98]},index=['A','B','C','D'])

df2 = pd.DataFrame({'C':[11,53],'D':[54,76]},index=['A','B'])

print(df2.join(df1,how="outer"))