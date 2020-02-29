import cv2

imgBGR  = cv2.imread('data/lena.jpg')

#cria uma borda branca de 20pixels na imagem
imgBGRWithBorder = cv2.copyMakeBorder(imgBGR,20,20,20,20,cv2.BORDER_CONSTANT,value=[255,255,255])

cv2.imshow('Border'       ,imgBGRWithBorder)

cv2.waitKey()
cv2.destroyAllWindows()

