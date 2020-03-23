import cv2
import numpy as np

img = cv2.imread('data/closing.png', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))


closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original', img)
cv2.imshow('Closing',  closing)

cv2.waitKey()
cv2.destroyAllWindows()

