import cv2
import numpy as np

img = cv2.imread('data/j.png', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))

erode = cv2.erode(img,kernel)
contorno = img - erode

cv2.imshow('Original',  img)
cv2.imshow('Contorno',  contorno)

cv2.waitKey()
cv2.destroyAllWindows()

