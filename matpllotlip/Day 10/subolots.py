import matplotlib.pyplot as plt

x =[1,3,5,3,7,8]
y=[2,3,1,5,4,6]


plt.subplot(2,2,1)
plt.title("line plot")
plt.plot(x,y,color = "r")


plt.subplot(2,2,2)
plt.title("pie chart")
plt.pie(x)


plt.subplot(2,2,3)
plt.title("Bar plat")
plt.bar(x,y,color='y')


plt.subplot(2,2,4)
plt.title("scatter plot")
plt.scatter(x,y,color='red')

plt.show()