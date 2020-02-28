import cv2


imgRGB  = cv2.imread('data/lena.jpg')
imgGray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)


#Numpy is a optimized library = fast array calculations. 
#So simply accessing each and every pixel values and modifyin it will be very slow and it is discouraged.


#get RGB pixel value at 100x100 
pixel = imgRGB[100,100]

#print rgb value of pixel
print('RGB value: ', pixel)

#get Gray pixel value at 100x100
pixel = imgGray[100,100]

#print gray scale value of pixel
print('Gray pixel: ', pixel)

#set green to position
imgRGB[100,100] = [0,255,0]

#set white to position
imgGray[100,100] = 255


cv2.imshow('RGB Edit pixel image',imgRGB)
cv2.imshow('Gray Edit pixel image',imgGray)

cv2.waitKey()
cv2.destroyAllWindows()

