# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 23:06:51 2021

@author: Sanjay
"""

# Import libraies
import cv2 as cv
import mediapipe as mp
import time

# Capture video
cap = cv.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Create a object from class hand
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# For frame rate
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                # if id == 4:
                #     cv.circle(img, (cx,cy), 10, (255,0,255), -1)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime + 0.00001

    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)


    cv.imshow('Image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
            break
  
cap.release()
cv.destroyAllWindows()