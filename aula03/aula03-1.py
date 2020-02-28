import cv2

img = cv2.imread('data/lena.jpg')

cv2.imshow('Img',img)

print('Shape: ', img.shape)
print('Size: ' , img.size)
print('Type: ' , img.dtype)

cv2.waitKey()

cv2.destroyAllWindows()

