import cv2 as cv
import numpy as np

img1 = cv.imread("./Images/girl1.jpg")
img2 = cv.imread("./Images/girl1.jpg")
img2Gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
print(img2Gray.shape)
arr = np.array(img2Gray)
# img2Gray3C = img2Gray.reshape([img2Gray[0], img2Gray[1]])
# print(img2Gray3C.shape)
arrRe = np.repeat(arr[:, :, np.newaxis], 3, axis=2)
print(arr.shape)
print(arrRe.shape)
imageStack = np.hstack([img1, arrRe])

while True:
    cv.imshow("image", imageStack)
    if cv.waitKey(0) & 0xFF == ord("q"):
        break