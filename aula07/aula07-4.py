# Standard imports
import cv2
import numpy as np

# Read image
img = cv2.imread("data/raio.png", cv2.IMREAD_COLOR)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 
#binary image
_,thresh = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY_INV)


#get contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

height, width = gray_image.shape
min_x, min_y  = width, height
max_x = max_y = 0


# computes the bounding box for the contour, and draws it on the frame,
for contour in contours :
    (x,y,w,h) = cv2.boundingRect(contour)
    print("x = ", x , " y= ", y , " w = ", w , " h = ", h )
    min_x, max_x = min(x, min_x), max(x+w, max_x)
    min_y, max_y = min(y, min_y), max(y+h, max_y)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)
   
   
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.polylines(img, [box] ,  True,  (0, 255, 0),  2)


    center = rect[0]
    angle = rect[2]
    print("Angle: ", angle)
    rows, cols = img.shape[0],img.shape[1]
    rot = cv2.getRotationMatrix2D(center, angle, 1)
    imgFinal = cv2.warpAffine(img, rot, (rows,cols))
    cv2.imshow("Angle: " + str(angle),  imgFinal)
    
cv2.imshow("Thresh ", thresh)
cv2.imshow("Blobs ",  img)


cv2.waitKey(0)