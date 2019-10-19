import cv2 
import numpy as np
img = cv2.imread('girl.jpg', 1)
print("Image height size: %d", img.shape[0])
print("Image weight size: %d", img.shape[1])
cv2.imshow("Image", img)
img_padding = np.zeros([300, 300, 3])

img_padding[50:274, 50:275,:] = img
print("Image height size:", img_padding.shape[0])
print("Image weight size: ", img_padding.shape[1])
cv2.imwrite('girl_padding.jpg', img_padding)
cv2.waitKey(0)
