# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:14:53 2021

@author: Sanjay
"""

# Import libraires
import cv2 as cv
import numpy as np

# Capture video
cap = cv.VideoCapture("./Videos/vtest.avi")
#cap = cv.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilate = cv.dilate(thresh, None, iterations=3)
    
    # Find contours
    contours, hy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for i in contours:
        x, y, w, h = cv.boundingRect(i)
        
        if cv.contourArea(i)<800:
            continue
        cv.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0), 2)
        text = "movement"
        cv.putText(frame1, f"Status : {text}", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
        
    # Draw contours to main frame
    #cv.drawContours(frame1, contours, -1, (255, 0, 0), 2)
    
    cv.imshow('video', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    
    if cv.waitKey(40) == 27:
        break
    
    
cv.destroyAllWindows()
cap.release()