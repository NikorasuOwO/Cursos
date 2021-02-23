import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

im = Image.open('magic-cube-1976725_640.jpg')
gray = np.mean(im, axis=2)
plt.imshow(gray, cmap='gray')
plt.show()

filt = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])

out = convolve2d(gray, filt)
plt.imshow(out)
plt.show()
