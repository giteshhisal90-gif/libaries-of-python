import matplotlib.pyplot as plt

x = [10,20,30,40]
y = ["C-programing","JAVA","Python","C++"]

plt.pie(x, labels=y ,radius = 1.2)


circle = plt.Circle((0,0), color="w", radius=0.7)
plt.gca().add_artist(circle)


# plt.pie([1],colors = "w",radius = 0.7)
plt.show()