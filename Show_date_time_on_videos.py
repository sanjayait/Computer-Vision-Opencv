import cv2
from datetime import datetime

# capture video
cap = cv2.VideoCapture(0)  # 0 - primary camera, 1,2 - secondary camera

# Check default resolution of web cam
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set width and height for frame
cap.set(3, 1280)
cap.set(4, 720)

# Read
while cap.isOpened():  # you can write "cap.isOpened()" in place "True"
    ret, frame = cap.read()
    if ret:
        datet = str(datetime.now())
        frame_text = cv2.putText(frame, datet, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        cv2.imshow('video', frame_text)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
