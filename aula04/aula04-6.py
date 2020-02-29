import cv2

imgBGR  = cv2.imread('data/lena.jpg')

#cria um ROI - Region of Interest
roi = imgBGR[200:400, 200:400]

final = imgBGR.copy()
final[0:200, 0:200] = roi


final[imgBGR.shape[0]-200:imgBGR.shape[0], 
      imgBGR.shape[1]-200:imgBGR.shape[1]] = roi 


cv2.imshow('BGR image',imgBGR)
cv2.imshow('ROI  mage',roi)
cv2.imshow('Final  mage',final)

cv2.waitKey()
cv2.destroyAllWindows()

