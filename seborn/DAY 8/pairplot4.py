import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

var = sns.load_dataset('tips')

# we use kind  = reg/scatter/kde/hist to change the type of plot in the pairplot. The default is scatter.

sns.pairplot(var,hue="sex",kind = "reg")
plt.show()