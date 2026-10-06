import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data_1=sns.load_dataset("penguins")

# print(data_1.head())

sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=data_1,hue="sex",style="sex")

plt.show()