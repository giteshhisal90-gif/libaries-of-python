import matplotlib.pyplot as plt
x =[2,4,6,8,10]
y = [1,2,3,4,5]



# when we have to convert solid line
plt.stem(x,y,linefmt=":",markerfmt="r*",bottom=0,label="python",orientation="horizontal")

plt.legend()
plt.show()