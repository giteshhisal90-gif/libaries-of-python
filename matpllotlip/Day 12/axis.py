import matplotlib.pyplot as plt

x=[2,5,3,6,7]
y=[3,2,6,5,7]

plt.plot(x,y)
plt.xticks(x,labels=['C','C++','python','java','web'])
plt.yticks(y)
plt.axis([0,10,0,7])
plt.show()