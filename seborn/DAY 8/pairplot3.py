import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

var = sns.load_dataset('tips')
sns.pairplot(var,hue="sex",x_vars=["total_bill", "tip"])
plt.show()