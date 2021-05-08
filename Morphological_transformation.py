# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:01:54 2021

@author: Sanjay
"""

# Import libraries
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

# Read image
img = cv.imread('./Images/smarties.png', 0)
ret, mask = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)

# Define kernal for dilation
kernal = np.ones((4, 4), np.uint8)
# Dilation
dilation = cv.dilate(mask, kernal, iterations=2)

# Erosion
erosion = cv.erode(mask, kernal, iterations=2)

# Opening
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)

# Closing
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)

# Gradient
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)

# Top-hat
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)
                         
titles = ['image', 'mask', 'dilation','erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(3, 3, i+1); plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]); plt.yticks([])
    
plt.show()
