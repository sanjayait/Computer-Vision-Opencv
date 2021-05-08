# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:41:46 2021

@author: Sanjay
"""

# Import libraries
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('./Images/opencv-logo-white.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernal)

# Blur Algorithim
blur = cv.blur(img, (5, 5))

# Gausian Blur used in high distorsion noise
gblur = cv.GaussianBlur(img, (5, 5), 0)

# Median Filter used in salt & pepper noise
mblur = cv.medianBlur(img, 5)

# BIlateral Filter border have preserved
blf = cv.bilateralFilter(img, 9, 75, 75)


titles = ['image', 'dst', 'blur', 'gblur', 'mblur','blf']
images = [img, dst, blur, gblur, mblur, blf]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]); plt.yticks([])
    
plt.show()