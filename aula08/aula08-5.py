#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/sudoku1.jpg',cv2.IMREAD_GRAYSCALE)


tresholdMin = 100
tresholdMax = 200


kernelSize = (5,5)

filtro = cv2.GaussianBlur(img,kernelSize,0)

edges = cv2.Canny(filtro,tresholdMin,tresholdMax)

cv2.imshow('Original', img)
cv2.imshow('Canny',edges)

cv2.waitKey()

cv2.destroyAllWindows()