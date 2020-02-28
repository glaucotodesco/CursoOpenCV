import cv2

imgRGB  = cv2.imread('data/lena.jpg')

#cria um ROI - Region of Interest
roi = imgRGB[200:400, 200:400]

final = imgRGB.copy()
final[0:200, 0:200] = roi


final[imgRGB.shape[0]-200:imgRGB.shape[0], 
      imgRGB.shape[1]-200:imgRGB.shape[1]] = roi 


cv2.imshow('RGB image',imgRGB)
cv2.imshow('ROI  mage',roi)
cv2.imshow('Final  mage',final)

cv2.waitKey()
cv2.destroyAllWindows()

