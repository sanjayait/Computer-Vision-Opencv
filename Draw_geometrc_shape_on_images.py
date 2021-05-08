import cv2
import numpy as np

# img = cv2.imread('lena.jpg', 1)

# Background color
img = np.zeros([512, 512, 3], np.uint8)

line = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 3)
arrow_line = cv2.arrowedLine(img, (100, 0), (255, 255), (255, 0, 0), 3)
# cv2.line(source, pt1, pt2, color(B,G,R), thickness)

rect = cv2.rectangle(img, (50, 50), (100, 100), (0, 255, 0), 3)
# cv2.rectangle(source, (x1, y1), (x2, y2), color(B, G, R), thickness)

cir = cv2.circle(img, (300, 300), 50, (0, 0, 255), -1)
# cv2.circle(source, center, radius, color(B,G,R), thickness)

font = cv2.FONT_HERSHEY_PLAIN
text = cv2.putText(img, 'Opencv', (200, 200), font, 3, (234, 160, 89), 1, 4)
# cv2.putText(source, text, origin, font, font_size, color(B,G,R), thickness, line_type)

cv2.imshow('window', text)
cv2.waitKey(0)
cv2.destroyAllWindows()