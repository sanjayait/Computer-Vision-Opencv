# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 02:07:04 2021

@author: Sanjay
"""

import numpy as np
import cv2 as cv

img = cv.imread('./Images/ab_de.jpg')
img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Threshhold image
ret, thresh = cv.threshold(img2, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of countour = " + str(len(contours)))

# Draw contours
cv.drawContours(img, contours, -1, (0, 255, 255), 3)

cv.imshow('image', img)
cv.imshow('image gray', img2)

cv.waitKey()
cv.destroyAllWindows()
