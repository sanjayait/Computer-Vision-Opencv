# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:55:25 2021

@author: Sanjay
"""

# Import libraries
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

# Read images
img = cv.imread('./Images/sudoku.png', 0)
# img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Laplacian method
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# Sobel-X and Sobel-Y
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0,  ksize=3)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1,  ksize=3)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# Sobel Combined
sobelCombined = cv.bitwise_or(sobelX, sobelY)

titles = ['image', 'lap', 'sobelX', 'sobelY', 'SobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]); plt.yticks([])
    
plt.show()