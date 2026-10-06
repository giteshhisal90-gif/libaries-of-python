import matplotlib.pyplot as plt

x = [2,4,6,8,10]
area1 = [3,4,9,6,7]
area2 = [1,2,3,4,5]
area3 = [2,3,8,5,6]

l=["area1", "area2", "area3"]
plt.stackplot(x, area1, area2, area3, labels=l)
plt.title("Stack Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()
plt.show()