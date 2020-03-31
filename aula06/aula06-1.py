import cv2

image = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE)
	
channels = [0]
histSize = [256]
ranges   = [0, 255]

hist = cv2.calcHist([image],channels,None,histSize,ranges)

for i, val in  zip(range(0,256), hist):
    print ("hist[",i,"]=", val)
    

cv2.waitKey()

cv2.destroyAllWindows()