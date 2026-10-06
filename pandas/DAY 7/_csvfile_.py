import pandas as pd

csv_1 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv")

print(csv_1)

n = csv_1.index
print(n)

p = csv_1.columns
print(p)

d = csv_1.describe()
print(d)