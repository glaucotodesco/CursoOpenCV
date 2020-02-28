import cv2

imgRGB  = cv2.imread('data/lena.jpg')

copy = imgRGB.copy()
ref  = imgRGB
roi  = imgRGB[200:400, 200:400]


imgRGB[0:200, 0:200] = 0
roi[:,:] = 255

cv2.imshow('imgRGB'       ,imgRGB)
cv2.imshow('Copy'         ,copy)
cv2.imshow('Ref'          ,ref)

cv2.waitKey()
cv2.destroyAllWindows()