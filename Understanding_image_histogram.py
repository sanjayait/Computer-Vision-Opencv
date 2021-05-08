# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:34:48 2021

@author: Sanjay
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./Images/lena.jpg', 0)
#img = np.zeros((200, 200), np.uint8)
#cv.rectangle(img, (0, 100), (200, 200), (255, 255, 255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
#b, g, r = cv.split(img)

hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

#cv.imshow('image', img)
#cv.imshow('blue', b)
#cv.imshow('green', g)
#cv.imshow('red', r)



#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])
plt.show()



cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()