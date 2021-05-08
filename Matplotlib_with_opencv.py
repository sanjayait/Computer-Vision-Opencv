# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:36:31 2021

@author: Sanjay
"""

import cv2 as cv
from matplotlib import pyplot as plt

# img = cv.imread('./Images/lena.jpg')
# img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Read image
img=cv.imread('./Images/gradient.png',0)
ret,th1=cv.threshold(img, 50, 200, cv.THRESH_BINARY)
ret,th2=cv.threshold(img, 50, 200, cv.THRESH_BINARY_INV)
ret,th3=cv.threshold(img, 50, 200, cv.THRESH_TRUNC)
ret,th4=cv.threshold(img, 50, 200, cv.THRESH_TOZERO)

titles = ['Original','Binary','Binary_inv','Trunc','Tozero']
images = [img, th1, th2, th3, th4]
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]); plt.yticks([])
plt.show()

