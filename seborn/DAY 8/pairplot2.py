import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

var = sns.load_dataset('tips')
sns.pairplot(var, vars=["total_bill", "tip"], hue="sex",hue_order=["Male", "Female"])
plt.show()