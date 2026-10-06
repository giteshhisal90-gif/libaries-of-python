import matplotlib.pyplot as plt
import numpy as np


x =["GITESH","YASH","OM","VIVEK","ASHUTOSH"]
y =[90,86,96,99,100]
z = [80,70,60,90,100]
width = 0.2

p = np.arange(len(x))
p1 =[i + width for i in p]


plt.xlabel("students",fontsize=15,color="blue")
plt.ylabel("Marks",fontsize=15,color="blue")
plt.title("Result Review",fontsize=20,color="red")

# when we want horizontal bar graph we just use barh instead of bar
plt.barh(p,y,width ,color = "red",label = "python")
plt.barh(p1,z,width ,color = "yellow",label = "java")

# we use yticks to change the position of y axis lable and we can also rotate the lable using rotation parameter
plt.yticks(p + width/2,x,rotation = 45)


plt.legend()
plt.show()