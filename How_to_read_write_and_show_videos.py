import cv2

# capture video
cap = cv2.VideoCapture(0)  # 0 - primary camera, 1,2 - secondary camera
# Video writer class
fourcc = cv2.VideoWriter_fourcc(*'MP42')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
# Read
while True:  # you can write "cap.isOpened()" in place "True"
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
