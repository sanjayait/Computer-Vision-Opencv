
import cv2 as cv
import numpy as np
from ImageStackModule import imageStack

img1 = cv.imread("./Images/lena.jpg")
img2 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img3 = cv.GaussianBlur(img2, (5, 5), 2)
img4 = cv.Canny(img3, 50, 100,)



# def imageStack(imgArray, scale):
#     sample = imgArray[0][0]
#     x, y, c = sample.shape
#     print(x, y, c)
#     resizArray1 = []
#     resizArray2 = []
#     for i, im in enumerate(imgArray[0]):
#         img = cv.resize(im, (x, y))
#         if len(img.shape) == 2:
#             img = np.repeat(img[:, :, np.newaxis], 3, axis=2)
#             img = cv.resize(img, None, fx=scale, fy=scale)
#             resizArray1.append(img)
#         else:
#             img = cv.resize(img, None, fx=scale, fy=scale)
#             resizArray1.append(img)
#
#     imgHor1 = np.hstack(resizArray1)
#
#     for i, im in enumerate(imgArray[1]):
#         img = cv.resize(im, (x, y))
#         if len(img.shape) == 2:
#             img = np.repeat(img[:, :, np.newaxis], 3, axis=2)
#             img = cv.resize(img, None, fx=scale, fy=scale)
#             resizArray2.append(img)
#         else:
#             img = cv.resize(img, None, fx=scale, fy=scale)
#             resizArray2.append(img)
#
#     imgHor2 = np.hstack(resizArray2)
#
#     imgStack = np.vstack([imgHor1, imgHor2])
#
#     return imgStack

while True:
    imgHor1 = imageStack([[img1, img2], [img3, img4]], 0.5)
    cv.imshow("imageStack", imgHor1)
    if cv.waitKey(0) & 0xFF == ord("q"):
        break
