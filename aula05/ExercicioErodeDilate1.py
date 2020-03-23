import cv2
import numpy as np

data =  np.array([
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,1,0,0],
                 [0,1,0,1,0],
                 [0,1,0,1,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 ], dtype = np.uint8
                 
                 )

ele = np.zeros((3,3),np.uint8)

ele.itemset((1,1),1)
ele.itemset((2,1),1)

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

