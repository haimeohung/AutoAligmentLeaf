import cv2 

img = cv2.imread('girl.jpg', 1)
print("Image height size: %d", img.shape[0])
print("Image weight size: %d", img.shape[1])
img_cropped = img[50:1500,0:150,:]
cv2.imshow("Image", img)
print("Image height size: %d", img_cropped.shape[0])
print("Image weight size: %d", img_cropped.shape[1])
cv2.imshow("cropped image", img_cropped)
cv2.waitKey(0)
