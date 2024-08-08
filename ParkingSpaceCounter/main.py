import cv2
import os

# Video file path
video_path = 'ParkingSpaceCounter/carPark.mp4'

# Check if the file exists
if not os.path.exists(video_path):
    print("Error: File not found. Check the file path and try again.")
    exit()

# Video feed
cap = cv2.VideoCapture(video_path)

# Check if video capture is initialized successfully
if not cap.isOpened():
    print("Error: Couldn't open video file.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Couldn't read the video stream.")
        break

    cv2.imshow('Image', img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
