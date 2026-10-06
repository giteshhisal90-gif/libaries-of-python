import matplotlib.pyplot as plt 

x = ["chem","python","BAI","AI"]
y = [90,86,96,99]

# for x axis lable 
plt.xlabel("subjects",fontsize=15,color="blue")

# for y axis lable
plt.ylabel("marks",fontsize=15,color="blue")

# for title of graph
plt.title("Result Review",fontsize=20,color="red")

# when we want different color of bars

c = ["red","green","blue","yellow"]

# when you want to chenge width use width parameter we can also change edge color and line width of bar using edgecolor and linewidth parameter
# we can change the linestyle of bar using linestyle parameter
# we use alpha parameter to change the transparency of bar
plt.bar(x,y,width=0.4,color=c,edgecolor = "black",linewidth = 2,linestyle = "--",alpha = 0.5,label ="chemistry")

# we can take lble using legend parameter and we can also change the location of legend using loc parameter
plt.legend()

plt.show()