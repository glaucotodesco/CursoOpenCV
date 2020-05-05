import cv2

img = cv2.imread("data/ruido.jpg", cv2.IMREAD_GRAYSCALE)

kernelSize = 5

filtro = cv2.medianBlur(img,kernelSize)


cv2.imshow('Original', img)
cv2.imshow('Media', filtro)

cv2.waitKey()

cv2.destroyAllWindows()