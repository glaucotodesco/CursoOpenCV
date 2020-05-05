import cv2
import numpy as np

data =  np.array([
                 [1,0,0,0],
                 [0,1,0,0],
                 [0,0,1,0],
                 [0,0,0,1],
                 ], dtype = np.uint8
                 
                 )

ele = np.array([
                 [0,0,0],
                 [0,1,0],
                 [0,1,0],
                 ], dtype = np.uint8
                 
                 )

erode  = cv2.erode(data,ele)


print('\n\nErode\n')
print(erode)

cv2.waitKey()
cv2.destroyAllWindows()

