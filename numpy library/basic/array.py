import numpy as np
from numpy import pi
# ar_zeros = np.zeros(4)
# print(ar_zeros)

# ar_zeros1 = np.zeros((2,3,4), dtype=np.int16)
# print(ar_zeros1)

# ar_ones = np.ones(4)
# print(ar_ones)

# ar_ones1 = np.ones((2,3,4))
# print(ar_ones1)

ar_dim = np.diag((1,1,1))
print(ar_dim)

ar_arrange = np.arange(4)
print(ar_arrange)

ar_shape = np.arange(15).reshape(3,5)
print(ar_shape)

ar_empty = np.empty(4)
print(ar_empty)

# ar_line = np.linspace(0,20,9) #0 to 20 ke bich ke 9 number
# print(ar_line)

x = np.linspace(0, 2 * pi, 100)        # useful to evaluate function at lots of points
f = np.sin(x)
print(f)