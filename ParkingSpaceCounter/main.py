import cv2
import os
import pickle
import numpy as np

# Video file path
video_path = 'ParkingSpaceCounter/carPark.mp4'

# Check if the file exists
if not os.path.exists(video_path):
    print("Error: File not found. Check the file path and try again.")
    exit()

# Video feed
cap = cv2.VideoCapture(video_path)

width, height = 107, 48


def checkParkingSpace():
    for pos in posList:
        x, y = pos

        imgCrop = img[y:y+height, x:x+width]
        cv2.imshow(str(x), imgCrop)


# Check if video capture is initialized successfully
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

    checkParkingSpace()
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width,
                      pos[1] + height), (255, 0, 255), 2)

    if not success:
        print("Error: Couldn't read the video stream.")
        break

    cv2.imshow('Image', img)
    cv2.imshow('ImageBlue', imgBlur)
    cv2.imshow('ImageThres', imgThreshold)

    # Exit on pressing 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
