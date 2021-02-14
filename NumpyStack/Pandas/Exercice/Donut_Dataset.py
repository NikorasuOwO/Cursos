import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Functions


def module(A):
    x2 = A[:, 0] ** 2
    y2 = A[:, 1] ** 2
    addition = x2 + y2
    return np.sqrt(addition)


# Creating lots of points

n = 2000  # number of points

A = np.random.uniform(-13, 13, (n, 2))
plt.scatter(A[:, 0], A[:, 1])
plt.show()

# Creating DataFrame
df = pd.DataFrame(data=A, index=None, columns=['x1', 'x2'])
df['x1^2'] = A[:, 0]**2
df['x2^2'] = A[:, 1]**2
df['x1*x2'] = A[:, 0] * A[:, 1]
df.to_csv('dataframe.csv', index=False, header=False)

# We will colorize the points whereby their distance
# to the point (0,0) is between two values ud1 & lw1 or two others ud2 & lw2.
# Creating two distinct groups of points.
# We start by making the "colorising array" as I like to call it.

# We will colorize the points if they meets two conditions regarding the
# module of the vector (0,0)-Point. The module of the vector has to be between
# ud and lw

lw1 = 7.5
up1 = 12.5
lw2 = 1.5
up2 = 6.5

mod = module(A)  # Array containing the module corresponding to each point

Ylw = np.array(mod > lw1)  # Module greater than lw1
Yup = np.array(mod < up1)  # Module less than up1

# An element is True if the point of corresponding index meets the conditions
Y1 = np.logical_and(Ylw, Yup)

# Same thing here
Ylw = np.array(mod > lw2)  # Module greater than lw2
Yup = np.array(mod < up2)  # Module less than up2
Y2 = np.logical_and(Ylw, Yup)
Y2_2 = Y2 * 2
# (We multiply by two to be able to differenciate the points from the 2 groups
#  later on in the scatter plot)

# We combine the two arrays, we combine the information regarding the 2 groups.
Y = Y1 + Y2_2
# print(str(Y))
# Scattering STEP 1
plt.scatter(A[:, 0], A[:, 1], c=Y)
plt.show()

# The separation starts, we'll make a new array with the colored points before
# STEP 2
OR = np.logical_or(Y1, Y2)

# print("OR: " + str(np.shape(np.logical_or(Y1, Y2))) + "A: "+str(np.shape(A)))
# print("OR: " + str(np.logical_or(Y1, Y2)) + "\n\n" + "A: " + str(A))

A = np.transpose(A)
C = A[:, np.logical_or(Y1, Y2)]
# print("C: " + str(np.shape(C)) + "A: " + str(np.shape(A)))
# print("C: " + str(C) + "\n\n" + "A: " + str(A))
C = np.transpose(C)
plt.scatter(C[:, 0], C[:, 1])
plt.show()

#### STEP 3 ###
# print("C: " + str(C))
Y = Y1 + Y2_2
# print("Y: " + str(Y))
# print("Y_tz: " + str(Y[Y != 0]))
Y = Y[Y != 0]  # We exclude the points with attribute 0 from the previous set
plt.scatter(C[:, 0], C[:, 1], c=Y)
plt.show()
