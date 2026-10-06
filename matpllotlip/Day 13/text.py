import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[2,1,4,3,5,6,7]

plt.plot(x,y)
plt.title("Python",fontsize=15)
plt.xlabel("x-axis",fontsize=15)
plt.ylabel("y-axis",fontsize=15)


plt.text(3,5,"Hello",fontsize=10,style="italic",bbox={"facecolor":"y"})
plt.annotate("java",xy=(2,1),xytext=(3,2),arrowprops=dict(facecolor="red",shrink=100))


plt.legend(["up"],facecolor="pink",edgecolor="black",loc = 9,shadow=True,framealpha=0.7)
plt.show()