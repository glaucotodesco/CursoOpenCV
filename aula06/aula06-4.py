import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE)

	
# create a mask to plot hist of this region
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255



# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(131), plt.imshow(img, 'gray')
plt.subplot(132), plt.imshow(mask,'gray')
plt.subplot(133), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
 
plt.show()





cv2.waitKey()

cv2.destroyAllWindows()