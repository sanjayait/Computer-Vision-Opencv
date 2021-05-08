# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:11:34 2021

@author: Sanjay
"""

import cv2 as cv

img = cv.imread('./Images/shapes2.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Find Threshold
ret, thresh = cv.threshold(imgGray, 225, 255, cv.THRESH_BINARY)
contours, hy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for i in contours:
    approx = cv.approxPolyDP(i, 0.01*cv.arcLength(i, True), True)
    cv.drawContours(img, [approx], 0, (255,0,0), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1]-5
    
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.90 and aspectRatio <= 1.10:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        else:    
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        
    elif len(approx) == 6:
        cv.putText(img, "Hexagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        
    elif len(approx) == 7:
        cv.putText(img, "Heptagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        
    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)


cv.imshow("Shapes", img)
#cv.imshow("thresh", thresh)
cv.waitKey(0)
cv.destroyAllWindows()