import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side

cv2.imshow('Imagem Normal - Imagem Equalizada',res)


# Calculate histogram with mask and without mask
# Check third argument for mask
histOriginal = cv2.calcHist([img],[0],None,[256],[0,256])
histEqualize = cv2.calcHist([equ],[0],None,[256],[0,256])

plt.subplot(121), plt.plot(histOriginal)
plt.subplot(122), plt.plot(histEqualize)
plt.show()



cv2.waitKey()

cv2.destroyAllWindows()