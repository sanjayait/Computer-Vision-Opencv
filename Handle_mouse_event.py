import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ",", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ',' + str(y)
        cv2.putText(img, strxy, (x, y), font, 0.5, (255, 0, 0), 1)
        cv2.imshow('window', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 0), 1)
        cv2.imshow('window', img)
        
# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('ab_de.jpg')
img = cv2.resize(img, (680, 420))
cv2.imshow('window', img)

cv2.setMouseCallback('window', click_event)

cv2.waitKey()
cv2.destroyAllWindows()

