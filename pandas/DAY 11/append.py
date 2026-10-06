import pandas as pd

df1 = pd.DataFrame({'A':[22,44,66,88],'B':[43,54,76,98]})

df2 = pd.DataFrame({'C':[11,53,44,65],'D':[54,76,43,65]})

print(df1.append(df2))