import cv2
from cvzone.HandTrackingModule import HandDetector
import math

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Loop
while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]['lmList']
        x1, y1 = lmList[5]
        x2, y2 = lmList[17]

    cv2.imshow("Image", img)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
