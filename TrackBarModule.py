import cv2 as cv


def nothing(x):
    pass


def initializeTrackbars(initiaTrackbarVal=0):
    cv.namedWindow('Trackbar')
    cv.resizeWindow('Trackbar', 360, 240)
    cv.createTrackbar('Threshold1', 'Trackbar', 100, 255, nothing)
    cv.createTrackbar('Threshold2', 'Trackbar', 100, 255, nothing)


def valTrackbars():
    Threshold1 = cv.getTrackbarPos('Threshold1', 'Trackbar')
    Threshold2 = cv.getTrackbarPos('Threshold2', 'Trackbar')
    src = Threshold1, Threshold2
    return src