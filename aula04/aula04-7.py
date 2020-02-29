import cv2

imgBGR  = cv2.imread('data/lena.jpg')
copy = imgBGR.copy()

#get b-g-r components
b,g,r = cv2.split(imgBGR)

#get blue component
b2 = imgBGR[:,:,0]

#set 0 to red compoment 
copy[:,:,2]=0;

cv2.imshow('Blue'       ,b)
cv2.imshow('Green'      ,g)
cv2.imshow('Red'        ,r)
cv2.imshow('Blue2'      ,b2)
cv2.imshow('Copy'       ,copy)


cv2.waitKey()
cv2.destroyAllWindows()

