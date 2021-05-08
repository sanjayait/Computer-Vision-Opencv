import cv2 as cv
import numpy as np
from ImageStackModule import imageStack

kernel = np.ones((6, 6), np.uint8)

img = cv.imread('BirdView.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv.Canny(imgBlur, 100, 200)
imgDilate = cv.dilate(imgCanny, kernel, iterations=2)

contours, hy = cv.findContours(imgDilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
contourAreaList = []
imgContour = img.copy()

while True:
    for i in contours:
        area = cv.contourArea(i)
        contourAreaList.append(area)
    sortContours = sorted(contours, key=cv.contourArea, reverse=True)
    biggestContour = sortContours[0]
    # if len(biggestContour) == 4:
    cv.drawContours(imgContour, biggestContour, -1, (255, 0, 0), 3)
    # print(list(contourList))
    imgstack = imageStack([[img, imgGray], [imgContour, imgCanny]], 0.5)
    cv.imshow("All in One", imgstack)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
