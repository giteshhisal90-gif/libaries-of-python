import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

var = [2,3,4,5,6,7]
var_1=[3,4,9,6,7,8]

# plt.plot(var,var_1)     ------>matplotlib

x = pd.DataFrame({"var":var,"var_1":var_1})
sns.lineplot(x="var",y="var_1",data=x)

plt.show()