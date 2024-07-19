import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialise the hand detector
detector = htm.handDetector(detectionCon=0.7)
colourR = (255, 0, 255)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if lmList:
        cursor = lmList[8]
        if 100 < cursor[0] < 300 and 100 < cursor[1] < 300:
            colourR = 0, 255, 0

    cv2.rectangle(img, (100, 100), (300, 300), colourR, cv2.FILLED)

    cv2.imshow("Image", img)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
