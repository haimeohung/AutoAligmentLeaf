import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Image/13.jpg',0)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
tmp_sobelx64f = abs_sobel64f.astype('uint8')
ret, otsu = cv2.threshold(tmp_sobelx64f, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(otsu,cmap = 'binary')
plt.title('Otsu'), plt.xticks([]), plt.yticks([])

plt.show()

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# # 1. Gray scale
# img = cv2.imread('Image/13.jpg', 0)
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# plt.subplot(2,2,1)
# plt.imshow(sobelx)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# plt.subplot(2,2,2)
# plt.imshow(sobely)
# # ret, otsu = cv2.threshold(sobelx, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# # plt.subplot(2,2,3)
# # plt.imshow(otsu)
# print(sobelx.shape[2])
# plt.show()
# cv2.waitKey(0)