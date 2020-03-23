import cv2


img = cv2.imread('data/opening.png', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('Original', img)
cv2.imshow('Opening',  opening)

cv2.waitKey()
cv2.destroyAllWindows()

