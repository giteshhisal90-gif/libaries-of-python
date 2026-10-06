import pandas as pd

df1 = pd.DataFrame({'A':[1,2,3,4,5,6,7,8,9,10],
                    'B':[11,12,13,14,15,16,17,18,19,20]})

df2 = pd.DataFrame({'A':[1,2,3,4,5,6,7,8,9,10],'c':[21,22,23,24,25,26,27,28,29,30]})

merge = pd.merge(df1,df2,on='A',indicator=True)

print(merge)

