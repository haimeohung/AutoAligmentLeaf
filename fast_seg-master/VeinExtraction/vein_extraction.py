import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1. Gray scale
origin = cv2.imread('Image/test.png', 1)
plt.subplot(2,3,1)

plt.imshow(origin)
plt.xlabel("Input image")
hsv = cv2.cvtColor(origin, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v = v / np.amax(v)
gray = (((h + 90) % 360)/360+1-v )/2 * 255
gray = gray.astype(int)
plt.subplot(2,3,6)

plt.imshow(gray)
plt.xlabel("Gray")
height_kernel,width_kernel, = 5,5
# 2.Morphological transform
kernel = np.ones((height_kernel,width_kernel),np.float32)/(height_kernel*width_kernel)
gray = gray.astype('uint8')
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
blackhat = tophat - blackhat
plt.subplot(2,3,2)
plt.imshow(blackhat, cmap = 'gray')
plt.xlabel("Transform")
# 3. Image enhancement
smallest = np.amin(blackhat)
biggest = np.amax(blackhat)
blackhat = 255 * (blackhat-smallest)/(biggest-smallest)

# 4. Otsu thresholding
blackhat = blackhat * 255
blackhat = blackhat.astype('uint8')
#cv2.Sobel(blackhat,cv2.CV_64F,1,0,ksize=5)
plt.subplot(2,3,3)
plt.imshow(blackhat, cmap = 'gray')
plt.xlabel("Before sobel")

ret, otsu = cv2.threshold(blackhat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#5. Linking discontinous line
otsu = otsu.astype('int')
for i in range(2, otsu.shape[0] - 2):
    for j in range(2, otsu.shape[1] - 2):
        if (otsu[i,j] == 0):           
            if ((otsu[i-1,j-1] + otsu[i-1,j] + otsu[i-1,j+1] + otsu[i,j-1] + otsu[i,j+1]
            + otsu[i+1,j-1] + otsu[i+1,j]+ otsu[i+1,j+1]) > 5 * 255):
                otsu[i,j] = 255
plt.subplot(2,3,4)
plt.imshow(otsu, cmap = 'gray')
plt.xlabel("Binarilize")

otsu = otsu.astype('uint8')

# 6. Elimatied isolated pixel
otsu = otsu / 255
kernel2 = np.ones((height_kernel-3, width_kernel-3), np.uint8) /((height_kernel-3)*(width_kernel-3))
opening = cv2.morphologyEx(otsu, cv2.MORPH_CLOSE, kernel2)

# 7. Show on origin image
for i in range(2, otsu.shape[0] - 2):
    for j in range(2, otsu.shape[1] - 2):
        if opening[i,j] == 1:
            origin[i,j, 0] = 255
            origin[i,j, 1] = 255
            origin[i,j, 2] = 255
plt.subplot(2,3,5)

plt.imshow(origin, cmap = 'gray')
plt.show()
plt.xlabel("Result")
cv2.waitKey(0)