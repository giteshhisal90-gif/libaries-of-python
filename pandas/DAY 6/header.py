import pandas as pd

csv = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv",header=2)
print(csv)

# i wanna to change name of heading

csv_1 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv",names=['col1','col2','col3'])
print(csv_1)


# i wanna to remove heading

csv2 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv",header=None)
print(csv2)

# i wanna to convert data type of specific coloum 

csv2 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv",dtype={"A":'float'})
print(csv2)
