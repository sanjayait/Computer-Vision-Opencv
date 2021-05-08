import cv2 as cv
import mediapipe as mp
import time

mpFaceDetection = mp.solutions.face_detection
mpDrawing = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

cap = cv.VideoCapture(0)
pTime = 0

while cap.isOpened():
    flag, frame = cap.read()
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = faceDetection.process(frameRGB)

    if results.detections:
        for detection in results.detections:
            ih, iw, channel = frame.shape
            # mpDrawing.draw_detection(frame, detection)
            # print(detection)
            x = int(detection.location_data.relative_bounding_box.xmin*iw)
            y = int(detection.location_data.relative_bounding_box.ymin*ih)
            w = int(detection.location_data.relative_bounding_box.width*iw)
            h = int(detection.location_data.relative_bounding_box.height*ih)
            print(x, y, w, h)
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
            cv.putText(frame, f"{int(detection.score[0] * 100)} %", (x, y - 20), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255),
                       2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(frame, f"FPS : {int(fps)}", (20, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
    cv.imshow('faces', frame)
    if cv.waitKey(2) == 27:
        break

cap.release()
cv.destroyAllWindows()