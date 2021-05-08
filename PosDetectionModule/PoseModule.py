# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:06:51 2021

@author: Sanjay
"""
# Import libraries

import cv2 as cv
import mediapipe as mp
import time

import numpy as np


class PoseDetector():
    def __init__(self, mode=False, up_body=False, smooth=True, detection_con=0.5, tracking_con=0.5):
        self.mode = mode
        self.up_body = up_body
        self.smooth = smooth
        self.detection_con = detection_con
        self.tracking_con = tracking_con

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose( self.mode, self.up_body, self.smooth, self.detection_con, self.tracking_con)

    def findPose(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPossition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for iD, lm in enumerate(self.results.pose_landmarks.landmark):
                 h, w, c = img.shape
                 cx, cy = int(lm.x * w), int(lm.y * h)
                 lmList.append([iD, cx, cy])
                 if draw:
                     cv.circle(img, (cx, cy), 7, (0, 0, 255), -1)

        return lmList




def main():
    cap = cv.VideoCapture(0)
    pTime = 0
    detector = PoseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPossition(img, draw=False)
        if len(lmList) != 0:
            print(lmList[14])
            cv.circle(img, (lmList[14][1], lmList[14][2]), 10, (0, 255, 255), -1)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime + 0.00001

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv.imshow('Image', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()




if __name__ == "__main__":
    main()