import cv2
import os
import pickle

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
        cv2.rectangle(img, pos, (pos[0] + width,
                      pos[1] + height), (255, 0, 255), 2)


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

    checkParkingSpace()

    if not success:
        print("Error: Couldn't read the video stream.")
        break

    cv2.imshow('Image', img)

    # Exit on pressing 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
