import cv2

# Read image
img = cv2.imread('lena.jpg', 1)  # 1- color image, 2- gray image, -1- unchanged(include alpha)
print(img)

# Display image
cv2.imshow('image', img)

# set keys
k = cv2.waitKey(0)  # 5000 are in milli-sec and '0' for always
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Write / save file
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
