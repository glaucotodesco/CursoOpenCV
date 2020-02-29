import cv2

imgBGR  = cv2.imread('data/lena.jpg')

copy = imgBGR.copy()
ref  = imgBGR
roi  = imgBGR[200:400, 200:400]


imgBGR[0:200, 0:200] = 0
roi[:,:] = 255

cv2.imshow('imgBGR'       ,imgBGR)
cv2.imshow('Copy'         ,copy)
cv2.imshow('Ref'          ,ref)

cv2.waitKey()
cv2.destroyAllWindows()