import cv2
import numpy as np

# read image
img = cv2.imread('ab_de.jpg')
lena = cv2.imread('lena.jpg')

img3 = cv2.resize(lena, (680, 420))
img2 = cv2.resize(img, (680, 420))
print(img2.shape)  # Return a tuple of number of rows and columns anc channel
print(img2.size)   # Return Total number of pixels is accessed
print(img2.dtype)  # Return image data type is obtained

# b, g, r = cv2.split(img)
# new = cv2.merge((b, g, r))

logo = img2[319:382, 289:412]
# logo = img2[y1:y2, x1:x2]

img2[50:113, 1:124] = logo
# img2[y1:y2, x1:x2] = logo

# Add two images
mix = cv2.add(img2, img3)

# Add weighted method
final = cv2.addWeighted(img3, .5, img2, .5, 0)

cv2.imshow('window', final)
cv2.waitKey(0)
cv2.destroyAllWindows()