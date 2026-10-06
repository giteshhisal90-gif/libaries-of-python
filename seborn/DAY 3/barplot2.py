import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

var = sns.load_dataset("penguins")
# print(var.head())

# TO BE A HORIZONTAL ORIENTATION BOTH SHOULD BE NUMERICAL

# sns.barplot(x="island",y="bill_length_mm",data=var,orient="h")

sns.barplot(x="island",y="bill_length_mm",data=var,orient="v",hue="sex",saturation=10,err_kws={'color':"y","linewidth":'12'})

plt.show()
