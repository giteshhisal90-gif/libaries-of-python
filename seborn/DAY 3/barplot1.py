import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

var = sns.load_dataset("penguins")
# print(var.head())


# when i want to set order
order_1=["Dream","Biscoe","Torgersen"]

sns.barplot(x="island",y="bill_length_mm",data=var,hue="sex",order=order_1,hue_order=["Female","Male"],ci=100)
plt.show()
