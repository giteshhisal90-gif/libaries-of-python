import matplotlib.pyplot as plt
import numpy as np
import random

data = np.random.randint(20,50,25)
l = [20,25,30,35,40,45,50]

plt.title("Histogram",fontsize = 20,color = "red")
plt.xlabel("Marks",fontsize = 15)
plt.ylabel("Frequency",fontsize = 15)

plt.hist(data,color ="red",edgecolor = "black",bins = l,cumulative = True,bottom = 20,align = "left",histtype="stepfilled",orientation="vertical",log=False,label="python") # cumulative = True will show the cumulative frequency of the data when we mark as false it will reverse the cumulative frequency of the data
# align = "left" will align the bars to the left side of the bin
# align = "right" will align the bars to the right side of the bin
# align = "mid" will align the bars to the middle of the bin

# we use histtype = "stepfilled" to fill the bars with color
# we use histtype ="step" to represent only steps 

# when i wanna  convert into log then i use parameter log = true


# plt.hist(data,"auto",(20,50),color ="red",edgecolor = "black")

plt.axvline(30,color = "g",linewidth = 3,label = "axvline")
plt.grid() #for grid lines
plt.legend()
plt.show()