import pandas as pd

dis = {'A':[1,2,3,4,5],'B':[6,7,8,9,0],'c':[1,2,3,4,5]}

d=pd.DataFrame(dis) 
print(d)

d.to_csv("text.csv")

# to convert csv without index

d.to_csv('text_new.csv',index=False)