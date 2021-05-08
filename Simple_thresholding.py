# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:38:09 2021

@author: Sanjay
"""

# Import libraries
import cv2 as cv
import numpy as np

# Read image
img=cv.imread('./Images/gradient.png',0)
ret,th1=cv.threshold(img, 50, 200, cv.THRESH_BINARY)
ret,th2=cv.threshold(img, 50, 200, cv.THRESH_BINARY_INV)
ret,th3=cv.threshold(img, 50, 200, cv.THRESH_TRUNC)
ret,th4=cv.threshold(img, 50, 200, cv.THRESH_TOZERO)

cv.imshow('window', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)

cv.waitKey(0)
cv.destroyAllWindows()