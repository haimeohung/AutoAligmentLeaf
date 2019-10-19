import cv2
import numpy as np
a = cv2.imread('girl.jpg', 1)
for i in range(a.shape[1] -1):
    for j in range(a.shape[0] -1):
        red = a[i, j, 0]
        green = a[i, j, 1]
        blue = a[i, j, 2]
        max1 = max(red, green, blue)
        if red == max1:
            a[i, j, 0] = 0
        if green == max1:
            a[i, j, 1] = 0
        if blue == max1:
            a[i, j, 2] = 0


cv2.imshow("test", a)
cv2.waitKey(0)
# #cv2.destroyAllWindows()
