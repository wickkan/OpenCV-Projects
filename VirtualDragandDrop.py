import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=2)
colourR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200

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
        # Extract x and y coordinates
        cursor_x, cursor_y = cursor[0], cursor[1]
        if cx - w // 2 < cursor_x < cx + w // 2 and cy - h // 2 < cursor_y < cy + h // 2:
            colourR = (0, 255, 0)
            cx, cy = cursor_x, cursor_y
        else:
            colourR = (255, 0, 255)

    cv2.rectangle(img, (cx - w // 2, cy - h // 2),
                  (cx + w // 2, cy + h // 2), colourR, cv2.FILLED)
    cv2.imshow("Image", img)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
