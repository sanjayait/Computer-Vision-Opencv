import cv2 as cv
import mediapipe as mp
import time
from HandTrackingModule import HandDetector


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