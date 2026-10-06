import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('tips')
sns.violinplot(x="day",y="total_bill", data=var,hue="time",linewidth=2,palette='Dark2')
plt.show()