# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:13:26 2021

@author: Sanjay
"""

# Import libraries
import cv2 as cv
import mediapipe
import time
import numpy as np
from HandTrackingModule import HandDetector
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Camera parameters
wCam, hCam = 640, 480

# Capture video
cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = HandDetector(detection_con=0.8, tracking_con=0.8)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    # Draw landmarks for hand points
    img = detector.find_hands(img)

    # Get location of landmarks
    lm_list = detector.find_position(img, draw=False)
    if len(lm_list) != 0:
        # print(lm_list[4], (lm_list[8]))

        x1, y1 = lm_list[4][1], lm_list[4][2]
        x2, y2 = lm_list[8][1], lm_list[8][2]
        cx, cy = (x1 + x2)//2 , (y1 + y2)//2

        cv.circle(img, (x1,y1), 7, (255, 0, 255), cv.FILLED)
        cv.circle(img, (x2,y2), 7, (255, 0, 255), cv.FILLED)
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv.circle(img, (cx, cy), 7, (255, 0, 255), cv.FILLED)

        length = math.hypot(x2-x1, y2-y1)

        # Hand range 25 - 275
        # Volume range -65 - 0

        vol = np.interp(length, [30, 270], [minVol, maxVol])
        volBar = np.interp(length, [30, 270], [400, 150])
        volPer = np.interp(length, [30, 270], [0, 100])
        print(int(length), int(vol))
        volume.SetMasterVolumeLevel(vol, None)

        if length < 30:
            cv.circle(img, (cx, cy), 7, (0, 255, 0), cv.FILLED)

    cv.rectangle(img, (50,150), (85, 400), (255, 0, 0), 3)
    cv.rectangle(img, (50,int(volBar)), (85, 400), (255, 0, 0), -1)
    cv.putText(img, f"{int(volPer)} %", (40, 450), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime + 0.0001
    
    cv.putText(img, str(int(fps)), (10, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()