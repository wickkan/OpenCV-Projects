import cv2
import pickle

img = cv2.imread('carParking.png')

while True:
    cv2.rectangle(img, (100, 100), (200, 150), (255, 0, 255), 2)
    cv2.imshow("image")
    cv2.waitKey(1)
