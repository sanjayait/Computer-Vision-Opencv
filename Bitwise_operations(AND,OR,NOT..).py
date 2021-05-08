# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:51:53 2021

@author: Sanjay
"""

import cv2 as cv
import numpy as np

# Create and read images
img=np.zeros([250,500,3], np.uint8)
img1=cv.rectangle(img,(200,0),(300,100),(255,255,255),-1)
img2=cv.imread("./Images/black&white.png")

#Bitwise Operators
#bitand=cv.bitwise_and(img1,img2)
#bitor=cv.bitwise_or(img1,img2)
bitxor=cv.bitwise_xor(img1,img2)
bitnot=cv.bitwise_not(img2)

# Show images
cv.imshow('img1',img1)
cv.imshow('img2',img2)
#cv.imshow('bitand',bitand)
#cv.imshow('bitor',bitor)
cv.imshow('bitxor',bitxor)
cv.imshow('bitnot',bitnot)

cv.waitKey(0)
cv.destroyAllWindows()
