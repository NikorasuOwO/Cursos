# Matrices #

import numpy as np

L = [[1, 2], [3, 4]]

print(str(L[0]))
print(str(L[1][1]))

A = np.array([[1, 2], [3, 4]])

print(str(A[0, 1]))

print(str(A[:, 0]))  # Returns column at index 0

print(str(A.T))  # Transpose of A

B = np.array([[0, 2], [2, 0]])

print(str(np.dot(A, B)))
# Multidimentional array multiplication is performed by the dot function

print(str(A * B))  # Element wise multiplication (!= dot product)

print(str(np.linalg.inv(A)))  # The inverse of a matrix

# the dim function

print(str(np.diag(A)))  # Returns the diagonal of A

print(str(np.diag(np.array([7, 2]))))  # Returns a matrix with the vector in its diagonal

# Eigen Values and Vectors

print("\n" + str(np.linalg.eig(A)))



input()
