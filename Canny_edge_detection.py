# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:45:09 2021

@author: Sanjay
"""

"""
The canny edge detection algorithm is composed 5 steps
1 - Noise reduction
2 - Gradient calculation
3 - Non maximum supression
4 - Double threshold
5 - Edge tracking by Hysteresis
"""

# Import libraries
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

# Read image
img = cv.imread('./Images/lena.jpg')
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Canny method
canny = cv.Canny(img, 100, 200, )


titles = ['image', 'canny']
images = [img2, canny]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]); plt.yticks([])
    
plt.show()