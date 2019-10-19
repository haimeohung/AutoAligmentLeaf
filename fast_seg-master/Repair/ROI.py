import cv2
import os, sys
import numpy as np


def ROI(img, roi):
    roi = cv2.resize(src= roi, dsize = (img.shape[1], img.shape[0]))
    thresh, roi = cv2.threshold(roi, 128, 1, type = cv2.THRESH_BINARY)
    new_img = img*np.abs(1-roi)
    return new_img

if __name__ == "__main__":
    assert len(sys.argv) == 3, '[USAGE] $ python opencv_ROI.py input_image roi_image'
    input_image_path, roi_image_path = sys.argv[1], sys.argv[2]
    
    assert os.path.isfile(input_image_path), 'Image not found @ %s' % input_image_path
    assert os.path.isfile(roi_image_path), 'ROI not found @ %s' % roi_image_path
    
    img = cv2.imread(input_image_path)       # shape: (588, 586, 3)
    roi = cv2.imread(roi_image_path)         # shape: (300, 300, 3)
    
    new_img = ROI(img, roi)
    
    cv2.imwrite('new_%s' % os.path.basename(input_image_path), new_img)
