import cv2
import pickle

img = cv2.imread('ParkingSpaceCounter/carParking.png')

if img is None:
    print("Error: Unable to load image. Check the file path and try again.")
    exit()

width, height = 107, 48
posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1+width and y1 < y < y1 + height:
                posList.pop(i)


cv2.namedWindow("image")
cv2.setMouseCallback("image", mouseClick)

while True:
    img_copy = img.copy()

    for pos in posList:
        cv2.rectangle(
            img_copy, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("image", img_copy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
