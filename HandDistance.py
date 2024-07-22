import cv2
from cvzone.HandTrackingModule import HandDetector

# webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# loop
while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
