### Dot product in numpy ###

import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

print(str(a * b))
print(str(np.sum(a * b)))  # That's the dot product

print(str(np.dot(a, b)))  # The proper way to do it

print(str(a @ b))  # The even cooler way.


# Lets find the cosine of the angle of 2 vectors

# cos(a,b) = dot(a,b) / magnitude of a * magnitude of b

dot = a @ b
mag_a = np.sqrt(np.sum(a**2))
mag_b = np.sqrt(np.sum(b**2))

print("cos = " + str(dot / (mag_a * mag_b)))

cos = dot / (mag_a * mag_b)

print("norm of a calculated properly: " + str(np.linalg.norm(a)))

print("angle in degrees: " + str(np.arccos(cos)))








input()
