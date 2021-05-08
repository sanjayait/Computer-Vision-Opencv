# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 23:06:51 2021

@author: Sanjay
"""

# Import libraies
import cv2 as cv
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, tracking_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.tracking_con = tracking_con

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.detection_con, self.tracking_con)
        self.mpDraw = mp.solutions.drawing_utils


    def find_hands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img


    def find_position(self, img, hand_no=0, draw=True):

        lm_list = []
        if self.results.multi_hand_landmarks:
            self.my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(self.my_hand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lm_list.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 7, (255, 0, 255), -1)
        return lm_list



def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lm_list = detector.find_position(img, draw=False)
        if len(lm_list) != 0:
            print(lm_list[4])

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