# Solving Linear Algebra #

import numpy as np

# x1 + x2 = 2200
# 1.5x1 + 4x2 = 5050

# Equation with matrices: A * X = b

A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])

print("sol: " + str(np.linalg.solve(A, b)))
#  These values are indeed proximations due to the way numpy solves the problem
