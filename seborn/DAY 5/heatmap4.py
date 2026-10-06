import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

y={'fontsize':'10','color':'b'}
var = np.linspace(1,10,20).reshape(5,4)


sns.heatmap(var,vmin=1,vmax=10,cmap="PuOr",annot=True,annot_kws=y,linecolor='black',linewidths=10,cbar=False,xticklabels=False,yticklabels=False)
plt.show()