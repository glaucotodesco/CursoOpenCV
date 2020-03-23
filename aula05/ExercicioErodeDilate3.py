import cv2
import numpy as np

data =  np.array([
                 [0,0,0,0,0],
                 [0,1,1,1,0],
                 [0,1,1,1,0],
                 [0,1,1,1,0],
                 [0,0,0,0,0],
                 [0,0,0,1,1],
                 [0,0,0,1,1],
                 ], dtype = np.uint8
                 
                 )

ele = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))


erode  = cv2.erode(data,ele,iterations=1,borderType=cv2.BORDER_CONSTANT,borderValue=0)
dilate = cv2.dilate(erode,ele)

print('Element\n')
print(ele)

print('\n\nOriginal\n')
print(data)
print('\n\nErode\n')
print(erode)
print('\n\nDilate\n')
print(dilate)

cv2.waitKey()
cv2.destroyAllWindows()

