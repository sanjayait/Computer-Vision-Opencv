# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:06:51 2021

@author: Sanjay
"""
# Import libraries

import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Create a object from class hand
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        for iD, lm in enumerate(results.pose_landmarks.landmark):
             h, w, c = img.shape
             cx, cy = int(lm.x * w), int(lm.y * h)
             print(id, cx, cy)
             if iD == 0:
                cv.circle(img, (cx, cy), 5, (255, 0, 255), -1)
             mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime + 0.00001

    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv.imshow('Image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

