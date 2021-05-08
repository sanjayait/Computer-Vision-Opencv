import cv2 as cv

# Read image
# img = cv.imread('lena.jpg')
cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Pre trained DNN model
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'frozen_inference_graph.pb'

# Set parameters
net = cv.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean(127.5)
net.setInputSwapRB(True)

while True:
    success, img = cap.read()
    # Extract parameter
    classIds, confs, bBox = net.detect(img, confThreshold=0.6)
    # print(classIds, bBox)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bBox):
            cv.rectangle(img, box, color=(255, 0, 0), thickness=2)
            cv.putText(img, classNames[classId-1], (box[0]+10, box[1]+30), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
            cv.putText(img, f"{str(int(confidence*100))}%", (box[0]+20, box[1]+50), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

    cv.imshow("objects", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
