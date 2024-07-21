import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=2)
colourR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200


class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # if the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor


rect = DragRect([150, 150])


while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)  # Updated method call

    if hands:
        for hand in hands:
            lmList = hand['lmList']  # Get the landmarks for each hand

            # Index finger tip
            index_finger = lmList[8][:2]  # (x, y)
            # Middle finger tip
            middle_finger = lmList[12][:2]  # (x, y)

            # Calculate distance
            length, info, img = detector.findDistance(
                index_finger, middle_finger, img)
            if length < 50:
                # Extract x and y coordinates of the index finger tip
                cursor = index_finger  # index finger tip landmark
                # call the update here
                rect.update(cursor)

    # Draw
    cx, cy = rect.posCenter
    w, h = rect.size
    cv2.rectangle(img, (cx - w // 2, cy - h // 2),
                  (cx + w // 2, cy + h // 2), colourR, cv2.FILLED)
    cv2.imshow("Image", img)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
