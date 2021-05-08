import cv2 as cv
import mediapipe as mp
import time

class FaceDetector():
    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDrawing = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, frame, draw=True):
        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.faceDetection.process(frameRGB)
        bBoxs = []
        if results.detections:
            for detection in results.detections:
                ih, iw, channel = frame.shape
                # mpDrawing.draw_detection(frame, detection)
                # print(detection)
                x = int(detection.location_data.relative_bounding_box.xmin*iw)
                y = int(detection.location_data.relative_bounding_box.ymin*ih)
                w = int(detection.location_data.relative_bounding_box.width*iw)
                h = int(detection.location_data.relative_bounding_box.height*ih)
                bBoxs.append([x, y, w, h, int(detection.score[0]*100)])
                if draw:
                    cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 1)
                    cv.putText(frame, f"{int(detection.score[0]*100)} %", (x, y-20), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)
        return frame, bBoxs

def main():
    cap = cv.VideoCapture(0)
    pTime = 0
    detector = FaceDetector()
    bBox = []
    while cap.isOpened():
        flag, frame = cap.read()
        frame, bBox = detector.findFaces(frame)
        print(bBox)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(frame, f"FPS : {int(fps)}", (20, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
        cv.imshow('faces', frame)
        if cv.waitKey(2) == 27:
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()