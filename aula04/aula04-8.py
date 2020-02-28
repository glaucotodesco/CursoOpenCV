import cv2

imgRGB  = cv2.imread('data/lena.jpg')

#cria uma borda branca de 20pixels na imagem
imgRGBWithBorder = cv2.copyMakeBorder(imgRGB,20,20,20,20,cv2.BORDER_CONSTANT,value=[255,255,255])

cv2.imshow('Border'       ,imgRGBWithBorder)

cv2.waitKey()
cv2.destroyAllWindows()

