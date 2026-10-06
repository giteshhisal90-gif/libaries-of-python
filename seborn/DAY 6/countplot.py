import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('tips')
sns.countplot(x="sex",data=var,hue="smoker",palette="bwr",saturation=0.5,edgecolor="black",linewidth=2)
plt.show()