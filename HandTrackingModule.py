import cv2
import mediapipe as mp
import time


class handDetector():

    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 4:  # tracking the tip of the thumb
                        cv2.circle(img, (cx, cy), 15,
                                   (255, 0, 255), cv2.FILLED)

                self.mpDraw.draw_landmarks(
                    img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img


cap.release()
cv2.destroyAllWindows()


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        if not success:
            print("Failed to capture image")
            break

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
