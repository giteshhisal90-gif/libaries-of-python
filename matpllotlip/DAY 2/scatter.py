import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [2,4,6,8,10,12,14]


plt.title("scatter plot",fontsize = 20,color = "red")
plt.xlabel("DAY",fontsize = 15)
plt.ylabel("Marks",fontsize = 15)

colors = ["red","blue","green","yellow","orange","pink","black"]


size = [100,200,300,400,500,600,700]


# using marker parameter we can change the shape of the scatter plot
plt.scatter(x,y,c=colors,s=size,alpha = 0.6,marker = "o",edgecolors = "black",linewidths = 2)
plt.show()