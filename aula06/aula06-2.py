import cv2
from matplotlib import pyplot as plt

image = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE)

	
channels = [0]
histSize = [256]
ranges   = [0, 255]

hist = cv2.calcHist([image],channels,None,histSize,ranges)


#image.ravel() transform image to vetor (one dimension)
plt.hist(image.ravel(),256,[0,256])
plt.show()




cv2.waitKey()

cv2.destroyAllWindows()