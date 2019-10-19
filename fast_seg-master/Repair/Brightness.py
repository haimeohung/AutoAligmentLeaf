import cv2
import sys
import numpy as np


def brightness(img, a, b):
    img_new = np.asarray(img*a+b, dtype=int)
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    return img_new


if __name__ == "__main__":
    a = 1
    b = 100
    if len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = int(sys.argv[2])
    img = cv2.imread('girl.jpg')
    img_new = brightness(img, a, b)
    cv2.imwrite('girl_brightness.jpg', img_new)
