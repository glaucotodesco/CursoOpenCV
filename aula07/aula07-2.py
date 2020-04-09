# Standard imports
import cv2
import numpy as np


# Read image
im = cv2.imread("data/blob.jpg", cv2.IMREAD_GRAYSCALE)
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
keypoints = detector.detect(im)

print("Blobs = ", len(keypoints))
for marker in keypoints:
    #center
    x,y = np.int(marker.pt[0]),np.int(marker.pt[1])
    pos = np.int(marker.size / 2)
    cv2.circle(im,(x,y),3,255,-1)
    cv2.rectangle(im,(x-pos,y-pos),(x+pos,y+pos),0,1)
    
cv2.imshow("Blobs = "+ str(len(keypoints)), im)

cv2.waitKey(0)