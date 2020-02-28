import cv2

cap = cv2.VideoCapture('data/sample.avi')

while cap.isOpened() :
    ret, frame = cap.read()

    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

