import cv2

ele1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
ele2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
ele3 = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

print(ele1,'\n')
print(ele2,'\n')
print(ele3,'\n')


cv2.waitKey()

cv2.destroyAllWindows()