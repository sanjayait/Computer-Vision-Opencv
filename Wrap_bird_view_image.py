import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./Images/BirdView.jpg")

width, height = 250, 350
pts1 = np.float32([[155, 294], [55, 194], [373, 186], [270, 105]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)

imgOutput = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("Image", img)
cv.imshow("Output", imgOutput)
cv.waitKey(0)
cv.destroyAllWindows()