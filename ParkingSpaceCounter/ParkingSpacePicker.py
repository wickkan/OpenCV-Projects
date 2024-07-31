import cv2
import pickle

# Load the image
img = cv2.imread('ParkingSpaceCounter/carParking.png')

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load image. Check the file path and try again.")
    exit()

while True:
    cv2.rectangle(img, (80, 230), (200, 150), (255, 0, 255), 2)
    cv2.imshow("image", img)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
cv2.destroyAllWindows()
