#https://docs.opencv.org/3.1.0/d5/d0f/tutorial_py_gradients.html

import cv2
import numpy as np

img = cv2.imread("data/bw.jpg", cv2.IMREAD_GRAYSCALE)


laplace = cv2.Laplacian(img,cv2.CV_8U)

sobelX = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
sobelY = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_64 = np.uint8(abs_sobel64f)


cv2.imshow('Original', img)
cv2.imshow('Laplace', laplace)
cv2.imshow('SobelX',  sobelX)
cv2.imshow('SobelY', sobelY)
cv2.imshow('Sobel64', sobel_64)



cv2.waitKey()

cv2.destroyAllWindows()