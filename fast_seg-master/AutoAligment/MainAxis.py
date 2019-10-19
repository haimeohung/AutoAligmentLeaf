import cv2 
import numpy as np
img = cv2.imread('1001.jpg', 0)
#img_resized = cv2.resize(img, dsize = (200, 200))
print("(", img.shape[1], img.shape[0], ")")

right = bot = 0
top = img.shape[0] - 1
left = img.shape[1] - 1

for i in range(img.shape[1] - 1):
    for j in range(img.shape[0] - 1):
        if (img[j, i] < 200) and ((i > right) or (j > bot)) :
            right = i
            bot = j
        if (img[j, i] < 200) and ((i < left) or (j < top)) :
            left = i
            top = j

print("(", right, bot, ")")
print("(", left, top, ")")
cv2.circle(img, center = (right, bot), radius = 2, thickness = 2, color = (0,0,0))
cv2.circle(img, center = (left, top), radius = 2, thickness = 2, color = (0,0,0))
cv2.line(img, pt1 = (left, top), pt2 = (right, bot), color = (0,0,0), thickness= 2)
cv2.imshow("a", img)
cv2.waitKey(0)