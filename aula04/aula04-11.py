import cv2

img1  = cv2.imread('data/lena.jpg')
aux = img1.copy()
aux[:,:] = 255
print('Aux1: ' , aux)

img2  = cv2.imread('data/lena.jpg')
aux = img2[:,:]
aux[:,:] = 255
print('Aux2: ' , aux)

img3  = cv2.imread('data/lena.jpg')
aux = img3
aux[0:100,0:100] = 255
print('Aux3: ' , aux)

img4  = cv2.imread('data/lena.jpg')
aux = img4
#perdeu a referencia para a imagem
aux = 255
print('Aux4: ' , aux)


cv2.imshow('img1'       ,img1)
cv2.imshow('img2'       ,img2)
cv2.imshow('img3'       ,img3)
cv2.imshow('img4'       ,img4)


cv2.waitKey()
cv2.destroyAllWindows()