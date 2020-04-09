# Standard imports
import cv2
import numpy as np


# Read image
img = cv2.imread("data/blob.jpg", cv2.IMREAD_COLOR)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 
#binary image
_,thresh = cv2.threshold(gray_image,220,255,cv2.THRESH_BINARY_INV)


#get contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

height, width = gray_image.shape
min_x, min_y  = width, height
max_x = max_y = 0


# computes the bounding box for the contour, and draws it on the frame,
for contour in contours :
    (x,y,w,h) = cv2.boundingRect(contour)
    print("x = ", x , " y= ", y , " w = ", w , " h = ", h )
    min_x, max_x = min(x, min_x), max(x+w, max_x)
    min_y, max_y = min(y, min_y), max(y+h, max_y)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)


cv2.imshow("Thresh ", thresh)
cv2.imshow("Blobs ",  img)

cv2.waitKey(0)