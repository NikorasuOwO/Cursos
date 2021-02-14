import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

im = Image.open('magic-cube-1976725_640.jpg')
gray_img = np.mean(im, axis=2)

print(str(gray_img[:, 0]))

Hx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
Hy = np.transpose(Hx)

Gx = convolve2d(gray_img, Hx)
Gy = convolve2d(gray_img, Hy)

G = np.sqrt(Gx**2 + Gy**2)

plt.subplot(3, 3, 1)
plt.imshow(im)
plt.subplot(3, 3, 2)
plt.imshow(gray_img, cmap='gray')
plt.subplot(3, 3, 3)
plt.imshow(255 - gray_img, cmap='gray')
plt.subplot(3, 3, 4)
plt.imshow(G, cmap='gray')

plt.subplot(3, 3, 5)
plt.imshow(Gx, cmap='gray')

plt.subplot(3, 3, 6)
plt.imshow(Gy, cmap='gray')

W = 255 - G
Wgx = 255 - Gx
Wgy = 255 - Gy
plt.subplot(3, 3, 7)
plt.imshow(W, cmap='gray')
plt.subplot(3, 3, 8)
plt.imshow(Wgx, cmap='gray')
plt.subplot(3, 3, 9)
plt.imshow(Wgy, cmap='gray')

plt.show()
