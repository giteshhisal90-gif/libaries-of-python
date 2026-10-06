import numpy as np
import time
 
time1=time.perf_counter()
arr = np.arange(1,9)**4
time2 = time.perf_counter()
print(time2-time1)
print(arr)

ti1=time.perf_counter()
l = [i**4 for i in range(1,9)]
ti2=time.perf_counter()
print(ti2-ti1)
print(l)


arr2 = np.arange(1,5)
print(arr2)