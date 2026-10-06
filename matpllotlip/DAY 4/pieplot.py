import matplotlib.pyplot as plt

x = [10,20,30,40]
y = ["C-programing","JAVA","Python","C++"]
ex = [0,0.1,0,0]
c = ["red","yellow","orange","green"]

# eplode is used to highlight the particular slice of the pie chart
# by using starangle we can rotate the pie chart  and change the starting position of the pie chart
# we can change center of pie chart by center parameter center = (0.5,0.5) like this
plt.pie(x, labels=y, explode=ex,colors=c,autopct = '%0.f%%',shadow=True,radius=1.2,labeldistance=1.3,startangle=90,textprops={'fontsize': 15, 'color': 'black'},counterclock=False,wedgeprops ={"linewidth": 1, "edgecolor": "black"},rotatelabels=False)


plt.title("Pie Chart",fontsize=20)
plt.legend(loc=2,fontsize=10)
plt.show()