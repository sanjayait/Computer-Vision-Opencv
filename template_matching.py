# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:11:16 2021

@author: Sanjay
"""

import cv2 as cv
import numpy as np

img = cv.imread('./Images/messi5.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

template = cv.imread('./Images/messi_face.png', 0)
w, h = template.shape[::-1]

res = cv.matchTemplate(imgGray, template, cv.TM_CCOEFF_NORMED)
#print(res)
threshold = 0.92
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w, pt[1]+h), (255, 0, 0), 1)


cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()