import cv2

capture = cv2.VideoCapture(0)

while True:
    success, frame = capture.read()

    cv2.imshow('camera', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break