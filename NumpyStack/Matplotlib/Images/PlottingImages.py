import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('vlc.png')
print("type: " + str(type(img)))  # Type isnt array-like

array = np.array(img)
print("type: " + str(np.shape(array)))  # Shape is (426, 640, 3)
# The image is indeed a 426 by 640 image colored in RGB

# plt.imshow(array)  # plt.imshow(img) would work too
# plt.show()

# Now we want a gray-scale image

gray = array.mean(axis=2)
# plt.imshow(gray)
# plt.show()

plt.imshow(gray, cmap='gray')
plt.show()
