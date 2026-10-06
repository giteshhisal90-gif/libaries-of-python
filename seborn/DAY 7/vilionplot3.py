import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('tips')
sns.violinplot(x="time",y="total_bill", data=var,hue='sex',split=True,inner='quart')
plt.show()