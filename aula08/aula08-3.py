import cv2

img = cv2.imread("data/CinqueTerre.jpg", cv2.IMREAD_COLOR)

kernelSize = (5,5)

filtro1 = cv2.GaussianBlur(img,kernelSize,0)
filtro2 = cv2.blur(img,kernelSize)

cv2.imshow('Original', img)
cv2.imshow('Gaussian', filtro1)
cv2.imshow('Blur', filtro2)


cv2.waitKey()

cv2.destroyAllWindows()