import cv2
import numpy as np

data =  np.array([
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,2,0],
                 [0,0,0,2,2,2],
                 [0,0,0,0,2,0],
                 ], dtype = np.uint8
                 
                 )

ele = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))


erode  = cv2.erode(data,ele)
dilate = cv2.dilate(data,ele)

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

