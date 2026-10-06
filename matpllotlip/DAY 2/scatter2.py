import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [2,4,6,8,10,12,14]
z = [10,20,30,40,50,60,70]


plt.title("scatter plot",fontsize = 20,color = "red")
plt.xlabel("DAY",fontsize = 15)
plt.ylabel("Marks",fontsize = 15)

# colors = ["red","blue","green","yellow","orange","pink","black"]


#  we can use range btween 0 to 100 for color 
colors =[10 ,40, 60, 80, 100, 20, 30]


size = [100,200,300,400,500,600,700]


# using marker parameter we can change the shape of the scatter plot
plt.scatter(x,y,c=colors,s =size,cmap = "viridis")
plt.scatter(x,z,c=colors,s =size,cmap = "plasma")  

plt.colorbar() # to show the color bar in the graph

plt.show()