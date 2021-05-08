import cv2
import cv2 as cv
import numpy as np

def empty(x):
    pass

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        # print(area)
        if area > 800:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            # print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 0, 255), 2)

img = cv.imread("./Images/shapes2.jpg")
imgContour = img.copy()
cv.namedWindow("Trackbar")
cv.createTrackbar("LowerThresh", "Trackbar", 50, 255, empty)
cv.createTrackbar("UpperThresh", "Trackbar", 100, 255, empty)

while True:
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
    lower = cv.getTrackbarPos("LowerThresh", "Trackbar")
    upper = cv.getTrackbarPos("UpperThresh", "Trackbar")
    imgCanny = cv.Canny(imgBlur, lower, upper)
    getContours(imgCanny)

    cv.imshow("image", img)
    # cv.imshow("gray", imgGray)
    # cv.imshow("blur", imgBlur)
    cv.imshow("canny", imgCanny)
    cv.imshow("contour", imgContour)
    if cv.waitKey(0) & 0xFF == ord("q"):
        break


cv.destroyAllWindows()