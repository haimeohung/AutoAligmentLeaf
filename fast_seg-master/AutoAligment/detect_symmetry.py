import cv2 
import numpy as np
import random
import math
from matplotlib import pyplot as plt
def lineFromPoints(P,Q): 
  
    a = Q[1] - P[1] 
    b = P[0] - Q[0]  
    c = a*(P[0]) + b*(P[1])  
    return a, b, c

def FineLine(img, ellipsis):
    center = ellipsis[0]
    point1_x = point2_x = int(ellipsis[0][0])
    point1_y = 0
    point2_y = img.shape[0] - 1

    #point1_x = int(point1_x * math.cos(ellipsis[2]* np.pi/180) - point1_y * math.sin(ellipsis[2]*np.pi/180) + center[0])
    #point1_y = int(point1_x * math.sin(ellipsis[2]* np.pi/180) + point1_y * math.cos(ellipsis[2]*np.pi/180) + center[1])

    return point1_x, point1_y, point2_x, point2_y

def rotate_image(mat, angle):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """

    height, width = mat.shape[:2] # image shape has 3 dimensions
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat




img = cv2.imread('Image/1299.jpg', 0)
mask = cv2.inRange(img, 0, 220)
_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
cv2.drawContours(img_rgb, contours, -1, (255, 0, 255), 3)


cv2.imshow("test", img_rgb)
maxx = 180
ellipse = []
for cnt in contours: 
    if len(cnt) < 5:
        continue  
    ellipse = cv2.fitEllipse(cnt)
    if (ellipse[2] < maxx):
        maxx = ellipse[2]
    print(ellipse[2])
    cv2.ellipse(img_rgb, ellipse, (0, 255, 0), 3)



img_rgb = rotate_image(img_rgb, maxx)
#point1_x, point1_y, point2_x, point2_y = FineLine(img_rgb, ellipse)
#cv2.line(img_rgb, (point1_x, point1_y), (point2_x, point2_y), (0, 255, 0), 3)
# for i in range(img_rgb.shape[1] - 1):
#     for j in range(img_rgb.shape[0] - 1):
#         if (img_rgb[j][i][0] == img_rgb[j][i][1] == img_rgb[j][i][2] == 0):
#             img_rgb[j][i] = (255,255,255)

cv2.imshow("test", img_rgb)
cv2.waitKey(0)
#cv2.destroyAllWindows()

