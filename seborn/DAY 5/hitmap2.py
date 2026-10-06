import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

var = sns.load_dataset("anagrams")
x = var.drop(columns="attnr").head(10)
sns.heatmap(x,vmin=1,vmax=10,cmap="PuOr")
plt.show()    