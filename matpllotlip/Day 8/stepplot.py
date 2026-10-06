import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[2,4,6,8,10,12,14,16,18]

plt.step(x,y,color ="violet",marker = "*" , ms = 10,mfc = "yellow",label = "python")


plt.title("Step Plot",fontsize = 20,color = "red")
plt.xlabel("X-axis",fontsize = 15)
plt.ylabel("Y-axis",fontsize = 15)


plt.grid()
plt.legend()
plt.show()