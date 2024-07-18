import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the hand detector
detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if lmList:
        print(lmList)

    cv2.imshow("Image", img)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
