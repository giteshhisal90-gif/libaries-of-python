import matplotlib.pyplot as plt

x =[2,4,6,8,10]
y = [3,4,5,6,7]

box = [x,y]

plt.boxplot(box,tick_labels=["python","c++"])
plt.show()