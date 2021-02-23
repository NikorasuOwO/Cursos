import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d


A = np.zeros([3, 3, 3])
A[0, 2, 1] = 1
print(str(A))
