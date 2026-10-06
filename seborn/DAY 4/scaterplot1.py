import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

var = sns.load_dataset("penguins").head(20)

# print(var.head())
# m={'Male':'o','Female':'*'}
# use markers parameter 
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=var,hue="sex",style="sex",sizes=(80,40))
plt.show()