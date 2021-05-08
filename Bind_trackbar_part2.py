# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:55:35 2021

@author: Sanjay
"""

import cv2 as cv
import numpy as np

# Callback function of trackbarr
def nothing(x):
    return None
    
# Create a black image and a window

cv.namedWindow('window')

# Create a Trackbar
cv.createTrackbar('CP','window',10,400,nothing)


# Create a Switch
switch="color/gray"
cv.createTrackbar('switch','window',0,1,nothing)

while(1):
    img=cv.imread('./Images/ab_de.jpg')
    pos=cv.getTrackbarPos('CP','window')
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(pos),(50,100),font,1,(255,0,0),1)
    
    k = cv.waitKey(1) & 0xFF
    if k==27:
        break
    
    # Get Trackbar values
    s=cv.getTrackbarPos('switch','window')
    
    if s==0:
        pass
    else:   
        # Set Trackbar values
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img=cv.imshow('window',img)   
cv.destroyAllWindows()