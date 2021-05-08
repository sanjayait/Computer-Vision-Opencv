import cv2
import numpy as np

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 255, 0), 3)
        cv2.imshow('window', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        myimg = np.zeros([512, 512, 3], np.uint8)
        myimg[:] = [blue, green, red]
        cv2.imshow('color', myimg)

# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('lena.jpg')

cv2.imshow('window', img)
points = []
cv2.setMouseCallback('window', click_event)

cv2.waitKey()
cv2.destroyAllWindows()

