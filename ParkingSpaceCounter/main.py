import cv2
import os
import pickle
import numpy as np
import cvzone

# Video file path
video_path = 'ParkingSpaceCounter/carPark.mp4'

# Check if the file exists
if not os.path.exists(video_path):
    print("Error: File not found. Check the file path and try again.")
    exit()

# Video feed
cap = cv2.VideoCapture(video_path)

width, height = 107, 48


def checkParkingSpace(imgPro):

    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y+height, x:x+width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            colour = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            colour = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0] + width,
                      pos[1] + height), colour, thickness)

    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50),
                       scale=3, thickness=5, offset=20, colorR=(0, 200, 00))


# Check if video capture is initialised successfully
if not cap.isOpened():
    print("Error: Couldn't open video file.")
    exit()

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)


while True:
    success, img = cap.read()

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrey, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)

    if not success:
        print("Error: Couldn't read the video stream.")
        break

    cv2.imshow('Image', img)

    # Exit on pressing 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
