import cv2
import numpy as np


img = cv2.imread('data/placa.png',cv2.IMREAD_COLOR)

# Copy the thresholded image.
floodfill = img.copy()

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)


seed        = (200,200)
colorToFill = (0,0,255)
minColor    = (60,90,8)
maxColor    = (70,100,10)

# Floodfill from point (0, 0)
cv2.floodFill(floodfill, mask, seed, colorToFill,minColor, maxColor)


cv2.imshow('Mask', mask)
cv2.imshow('Original', img)
cv2.imshow('floodfill',floodfill)

cv2.waitKey()

cv2.destroyAllWindows()