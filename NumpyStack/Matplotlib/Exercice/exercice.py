# Exercice #

import numpy as np
import matplotlib.pyplot as plt
import math

#  Generating data
n = 10000  # Number of points
P = np.random.uniform(-1, 1, (n, n))  # 50 points with 2 coordinates
xcoords = P[:, 0]
ycoords = P[:, 1]

# Label array
L = np.zeros(np.shape(P)[0])

L[:] = np.logical_xor(np.ceil(xcoords[:]), np.ceil(ycoords[:]))
# Using ceiling to "convert" <0 numbers to 0 and >0 to one
# Then logical_xor computes the XOR operation element-wise

plt.scatter(xcoords, ycoords, c=L)
plt.show()
# print("L: " + str(L))
# print("xc: " + str(np.ceil(xcoords[:])))
# print("xy: " + str(np.ceil(ycoords[:])))
