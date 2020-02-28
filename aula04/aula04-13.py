import cv2
import numpy as np

board = np.zeros((320,320), np.uint8)
white = np.zeros((40,40), np.uint8)
white[:,:] = 255

for lin in range(0,8):
    for col in range(0,8):
        if lin % 2 == 0 and col % 2 == 0:
            board[lin*40:lin*40+40, col*40:col*40+40] = white
        else:
            if lin % 2 == 1 and col % 2 == 1:    
               board[lin*40:lin*40+40, col*40:col*40+40] = white


cv2.imshow('Chess Board'       ,board)

cv2.waitKey()
cv2.destroyAllWindows()