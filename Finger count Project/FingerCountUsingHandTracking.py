# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:35:27 2021

@author: Sanjay
"""

# Import libraries
import cv2 as cv
import os
import time
import HandTrackingModule as htm


wCam, hCam = 640, 480
cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

folder = 'Images'
myList = os.listdir(folder)
print(myList)

overlayList = []
for imPath in myList:
    img = cv.imread(f'{folder}/{imPath}')
    img = cv.resize(img, (150, 175))
    overlayList.append(img)
    
detector = htm.HandDetector(detection_con=0.75)
tipsIds = [4, 8, 12, 16, 20]

while True:
    flag, img = cap.read()
    img = detector.find_hands(img)
    lmList = detector.find_position(img, draw=False)
    
    if len(lmList) != 0:
        fingers = []
         
        # Thumb
        if lmList[tipsIds[0]][1] > lmList[tipsIds[0]-1][1]:
                fingers.append(1)
        else:
            fingers.append(0)
        # 4 Fingers        
        for id in range(1, 5):
            if lmList[tipsIds[id]][2] < lmList[tipsIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        totalFingures = fingers.count(1)
        #print(totalFingures)
        img[0:175, 0:150] = overlayList[totalFingures-1]
        cv.rectangle(img, (0, 180), (150, 250), (0, 255, 0), -1)
        cv.putText(img, str(totalFingures), (60, 235), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 4)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime + 0.0001
    cv.putText(img, f"{int(fps)}", (165, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0, 1))
    cv.imshow('image', img)
    if cv.waitKey(2) == 27:
        break
    
cap.release()
cv.destroyAllWindows()