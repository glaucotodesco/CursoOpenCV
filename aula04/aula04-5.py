import cv2

imgBGR  = cv2.imread('data/lena.jpg')

#get red value of pixel at 100x100 
red = imgBGR.item(100,100,2);

#print BGR value of pixel
print('Red value: ', red)

#set red new valeu
imgBGR.itemset((100,100,2),255);

cv2.imshow('BGR Edit pixel image',imgBGR)

cv2.waitKey()
cv2.destroyAllWindows()

