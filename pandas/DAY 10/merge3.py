import pandas as pd

d1 = pd.DataFrame({'A':[1,2,3,4,5,6,7,8,9,10],
                   'B':[11,12,13,14,15,16,17,18,19,20]})  

d2 = pd.DataFrame({'A':[1,2,3,4,5,6,7,8,9,10],
                   'C':[21,22,23,24,25,26,27,28,29,30]})

merge = pd.concat([d1,d2],axis = 1)
print(merge)