import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

var = np.array([["a1","a2","a3","a4"],["b1","b2","b3","b4"]])


sns.heatmap(var,vmin=0,vmax=10,cmap="PuOr",annot=var,fmt="S")
plt.show()