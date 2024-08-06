import cv2
import pickle

# Load the image
img = cv2.imread('ParkingSpaceCounter/carParking.png')

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load image. Check the file path and try again.")
    exit()

width, height = 107, 48
posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))


while True:
    cv2.setMouseCallback("Image", mouseClick)
    # cv2.rectangle(img, (50, 192), (157, 240), (255, 0, 255), 2)
    cv2.imshow("image", img)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
cv2.destroyAllWindows()
