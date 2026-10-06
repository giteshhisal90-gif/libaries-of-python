import pandas as pd

# csv = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv")

# print(csv)

# csv_1 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv",nrows=3)
# print(csv_1) 
# print(type(csv_1))

# i wanaa to get only one column
csv_2 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv",usecols=['A','B'])
# print(csv_2)

# csv_3 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\employee_data (1).xlsx")
# print(csv_3)

# instead of giving name of coloumns i can give a number of index

# csv_4 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv",usecols=[0,1])
# print(csv_4)

# whwn i wanna to skip rows 


print()
csv_5 = pd.read_csv("C:\\Users\\jijau\\OneDrive\\Desktop\\python library\\pandas\\text_new.csv",skiprows=[0,3])
print(csv_5)