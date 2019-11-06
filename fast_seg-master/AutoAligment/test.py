import cv2 
import numpy as np
import random
import math
import os
from matplotlib import pyplot as plt
import random
import glob

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
    rotated_mat[np.where((rotated_mat<=[50,50,50]).all(axis=2))] = [255,255,255]
    return rotated_mat



def auto_rotate(img_rgb):
    # read
    img_rgb = cv2.resize(img_rgb, (200, 200))
    img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
    # filter
    mask = cv2.inRange(img, 0, 220)
    # find contours
    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contour = max(contours, key = cv2.contourArea)
    hull = cv2.convexHull(contour, False)
    # create an empty black image
    drawing = np.zeros((mask.shape[0], mask.shape[1], 3), np.uint8)
    # draw contours and hull points
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    cv2.drawContours(drawing, contours, 0, color_contours, 1, 8, hierarchy)
    cv2.drawContours(drawing, hull, 0, color, 1, 8)
    ellipse = cv2.fitEllipse(hull)
    cv2.ellipse(drawing, ellipse, (0, 255, 0), 1)
    img_rgb = rotate_image(img_rgb, ellipse[2])
    return img_rgb, drawing, ellipse[2]

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images



#for img in load_images_from_folder('Random'):
mean = 0.0
i = 0
j = 0
for filename in glob.glob(os.path.join('Random', '*.jpg')):
    raw = filename[7:len(filename)]
    raw_1 = raw[0: len(raw)-4]
    angle, name = raw_1.split('_')
    img = cv2.imread(filename)
    _ , _ , angle_res = auto_rotate(img)
    variance = abs(angle_res - int(angle))
    if variance > 90:
        j += 1
    mean += variance
    i += 1
print(mean/i)
print(i, j)
cv2.waitKey(1)