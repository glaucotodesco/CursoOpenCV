import cv2
import numpy as np

img = np.zeros((400,400,3), np.uint8)

#formato BGR
img[:,:] = (255,0,0)

cv2.imshow('img'       ,img)

cv2.waitKey()
cv2.destroyAllWindows()