import matplotlib.pyplot as plt

x = [10,20,30,40,50,90]
# outler show dta go outside

# notch parameter for notch and vert is true men vertica and false mean horrizontal

# whis parameter join the outler

# sym give coler and shape of the outler


plt.boxplot(x,notch=False,vert=True,widths=0.1,tick_labels=["python"],patch_artist=True,showmeans=True,whis=1.5,sym="r*",boxprops=dict(color = "red"),capprops=dict(color = "gold"),whiskerprops=dict(color = "pink"),flierprops = dict(markerfacecolor = "green"))


plt.show()