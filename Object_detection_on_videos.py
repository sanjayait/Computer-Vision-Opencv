# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:32:47 2021

@author: Sanjay
"""

# Import libraries
import cv2 as cv
import numpy as np

# Callback function for trackbar
def nothing(x):
    pass

# Capture video
cap=cv.VideoCapture(0)
# Create a window
cv.namedWindow('tracking')
cv.createTrackbar('LH','tracking',0,255,nothing)
cv.createTrackbar('LS','tracking',0,255,nothing)
cv.createTrackbar('LV','tracking',0,255,nothing)
cv.createTrackbar('UH','tracking',255,255,nothing)
cv.createTrackbar('US','tracking',255,255,nothing)
cv.createTrackbar('UV','tracking',255,255,nothing)


while True:
    ret, img=cap.read()
    
    # Convert image to HSV color space
    hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    # Get trackbar possition
    l_h=cv.getTrackbarPos('LH','tracking')
    l_s=cv.getTrackbarPos('LS','tracking')
    l_v=cv.getTrackbarPos('LV','tracking')
    
    u_h=cv.getTrackbarPos('UH','tracking')
    u_s=cv.getTrackbarPos('US','tracking')
    u_v=cv.getTrackbarPos('UV','tracking')
    
    l_b=np.array([l_h, l_s, l_v])
    u_b=np.array([u_h, u_s, u_v])
    
    # define mask
    mask=cv.inRange(hsv, l_b, u_b,)
    
    # Resultant image
    res=cv.bitwise_and(img,img, mask=mask)
    
    # Show images
    cv.imshow('img',img)
    # cv.imshow('mask',mask)
    cv.imshow('res',res)
    
    key=cv.waitKey(1)
    if key==27:
        break
    
cap.release()
cv.destroyAllWindows()