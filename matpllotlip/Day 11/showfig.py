import matplotlib.pyplot as plt


x=[1,2,3,4,5,6]
y=[3,2,1,6,5,7]


plt.plot(x,y,color="r")
plt.savefig('line plot',dpi=2000,facecolor='g',transparent=True,bbox_inches = "tight")
plt.show()