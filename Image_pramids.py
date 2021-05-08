# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 00:01:16 2021

@author: Sanjay
"""

# Import libraries
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv.imread('./Images/ab_de.jpg')
layer = img.copy()
gp = [layer]

for i in range(5):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    #cv.imshow(str(i), layer)
    

for i in range(4, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    plt.imshow(laplacian)
    

plt.imshow(img)
plt.show()