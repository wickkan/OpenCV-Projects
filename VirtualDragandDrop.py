import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=2)
colourR = (255, 0, 255)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)  # Updated method call

    if hands:
        lmList = hands[0]['lmList']  # Get the first hand detected
        cursor = lmList[8]  # Index finger tip
        if 100 < cursor[0] < 300 and 100 < cursor[1] < 300:
            colourR = (0, 255, 0)
        else:
            colourR = (255, 0, 255)

    cv2.rectangle(img, (100, 100), (300, 300), colourR, cv2.FILLED)
    cv2.imshow("Image", img)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
