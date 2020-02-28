import cv2

imgRGB  = cv2.imread('data/lena.jpg')
copy = imgRGB.copy()

#get b-g-r components
b,g,r = cv2.split(imgRGB)

#get blue component
b2 = imgRGB[:,:,0]

#set 0 to green compoment 
copy[:,:,2]=0;

cv2.imshow('Blue'       ,b)
cv2.imshow('Green'      ,g)
cv2.imshow('Red'        ,r)
cv2.imshow('Blue2'      ,b2)
cv2.imshow('Copy'       ,copy)


cv2.waitKey()
cv2.destroyAllWindows()

