import cv2

img = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Img',img)

cv2.imwrite('newfile.jpg', img)

print('Gray Image Save')

cv2.waitKey()


cv2.destroyAllWindows()

