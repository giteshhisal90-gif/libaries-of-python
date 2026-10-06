import matplotlib.pyplot as plt

x =[1,2,3,4,5,6,7,8,9]
y = [2,4,6,8,10,12,14,16,18]

plt.plot(x,y,color = "red")

plt.title("Fill Between",fontsize = 20,color = "red")
plt.xlabel("X-axis",fontsize = 15)
plt.ylabel("Y-axis",fontsize = 15)  

# plt.fill_between(x,y)
plt.fill_between(x=[4,6],y1=4,y2=16,color = "yellow",alpha = 0.5,label = "python")



plt.legend()
plt.show()
