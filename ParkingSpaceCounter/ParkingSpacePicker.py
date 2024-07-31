import cv2
import pickle

img = cv2.imread('carParking.png')

while True:
    cv2.imshow("image")
    cv2.waitKey(1)
