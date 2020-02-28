import cv2

#Para instalar se necessario: pip install matplotlib
from matplotlib import pyplot as plt

img1  = cv2.imread('data/lena.jpg')

RED = [255,0,0]

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=RED)

# plt.subplot(2,3, X )
# Cria um plot de tamanho 2 x 3 (6 Posicoes).
# X e a posicao ocupada (valores de 1 a 6)

plt.subplot(2,3,1),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(2,3,2),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(2,3,3),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

