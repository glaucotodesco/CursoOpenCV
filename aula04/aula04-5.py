import cv2

imgRGB  = cv2.imread('../data/lena.jpg')

#get red value of pixel at 100x100 
red = imgRGB.item(100,100,2);

#print rgb value of pixel
print('Red value: ', red)

#set red new valeu
imgRGB.itemset((100,100,2),255);

cv2.imshow('RGB Edit pixel image',imgRGB)

cv2.waitKey()
cv2.destroyAllWindows()

