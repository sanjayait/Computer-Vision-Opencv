# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:55:35 2021

@author: Sanjay
"""

import cv2 as cv
import numpy as np

# Callback function of trackbarr
def nothing(x):
    #print(x)
    
# Create a black image and a window
img=np.zeros([300,512,3],np.uint8)
cv.namedWindow('window')

# Create a Trackbar
cv.createTrackbar('B','window',0,255,nothing)
cv.createTrackbar('G','window',0,255,nothing)
cv.createTrackbar('R','window',0,255,nothing)

# Create a Switch
switch="0 : OFF\n 1 : ON"
cv.createTrackbar('switch','window',0,1,nothing)

while(1):
    cv.imshow('window',img)
    k = cv.waitKey(1) & 0xFF
    if k==27:
        break
    
    # Get Trackbar values
    b=cv.getTrackbarPos('B','window')
    g=cv.getTrackbarPos('G','window')
    r=cv.getTrackbarPos('R','window')
    s=cv.getTrackbarPos('switch','window')
    
    if s==0:
        img[:]=0
    else:   
        # Set Trackbar values
        img[:]=[b,g,r]
        
cv.destroyAllWindows()