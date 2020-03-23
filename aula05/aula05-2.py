import cv2
from matplotlib import pyplot as plt


img = cv2.imread('data/j.png', cv2.IMREAD_GRAYSCALE)

ele1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
ele2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
ele3 = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

erode1 = cv2.erode(img,ele1)
erode2 = cv2.erode(img,ele2)
erode3 = cv2.erode(img,ele3)

plt.subplot(2,2,1),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(2,2,2),plt.imshow(erode1,'gray'),plt.title('CROSS')
plt.subplot(2,2,3),plt.imshow(erode2,'gray'),plt.title('ELLIPSE')
plt.subplot(2,2,4),plt.imshow(erode3,'gray'),plt.title('RECT')

plt.show()


cv2.waitKey()
cv2.destroyAllWindows()

