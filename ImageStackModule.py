import cv2 as cv
import numpy as np

def imageStack(imgArray, scale):
    sample = imgArray[0][0]
    x, y, c = sample.shape
    # print(x, y, c)
    resizArray1 = []
    resizArray2 = []
    for i, im in enumerate(imgArray[0]):
        img = cv.resize(im, (x, y))
        if len(img.shape) == 2:
            img = np.repeat(img[:, :, np.newaxis], 3, axis=2)
            img = cv.resize(img, None, fx=scale, fy=scale)
            resizArray1.append(img)
        else:
            img = cv.resize(img, None, fx=scale, fy=scale)
            resizArray1.append(img)

    imgHor1 = np.hstack(resizArray1)

    for i, im in enumerate(imgArray[1]):
        img = cv.resize(im, (x, y))
        if len(img.shape) == 2:
            img = np.repeat(img[:, :, np.newaxis], 3, axis=2)
            img = cv.resize(img, None, fx=scale, fy=scale)
            resizArray2.append(img)
        else:
            img = cv.resize(img, None, fx=scale, fy=scale)
            resizArray2.append(img)

    imgHor2 = np.hstack(resizArray2)

    imgStack = np.vstack([imgHor1, imgHor2])

    return imgStack


def main():
    pass

if __name__ =="__main__":
    main()