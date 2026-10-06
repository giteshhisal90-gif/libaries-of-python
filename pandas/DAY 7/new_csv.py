import pandas as pd

csv = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv")
print(csv)


# if want use selectead data 3 reprent how many rows you want
head = csv.head(3)
print(head)