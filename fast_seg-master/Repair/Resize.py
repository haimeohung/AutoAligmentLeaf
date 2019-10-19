import cv2 

img = cv2.imread('girl.jpg', 1)
print("Image height size: %d", img.shape[0])
print("Image weight size: %d", img.shape[1])
img_resized = cv2.resize(img, (100, 200))
cv2.imshow("Image", img)
print("Image height size: %d", img_resized.shape[0])
print("Image weight size: %d", img_resized.shape[1])
cv2.imshow("Resized image", img_resized)
cv2.waitKey(0)
