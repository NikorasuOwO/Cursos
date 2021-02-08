# Timing and comparing two matrix multiplication computing methods

import numpy as np
import time

scale = 1000
n = 3
repetitions = 100000


def lmatrix(n, scale):

    # Matrix creation:
    A = [0] * n
    for i in range(0, n):
        A[i] = []
        for j in range(0, n):
            A[i].append(np.random.random() * scale)

    return A


def npmatrix(n, scale):
    return np.random.random((n, n)) * scale


def multLM(A, B):
    C = [[0] * n] * n
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]


startLM = time.time()

for i in range(0, repetitions):
    A = lmatrix(n, scale)
    B = lmatrix(n, scale)
    C = multLM(A, B)

endLM = time.time()
timeLM = endLM - startLM

startNP = time.time()
for i in range(0, repetitions):
    A = npmatrix(n, scale)
    B = npmatrix(n, scale)
    C = A.dot(B)

endNP = time.time()
timeNP = endNP - startNP

print("timeLM: " + str(timeLM) + " | " + "timeNP: " + str(timeNP))
print("RATIO (LM/NP): " + str(timeLM / timeNP))
