import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

var = sns.load_dataset("penguins")
print(var.head())

# sns.displot(var["bill_length_mm"],bins=[170,180,190,200,210,220,230,240])


sns.displot(var["bill_length_mm"],kde=True,rug=True,color="r")
plt.show()