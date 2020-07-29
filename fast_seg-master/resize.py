import cv2

def resize(img):
    dim = (256,256)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)



input = cv2.imread("./braces.png",cv2.IMREAD_UNCHANGED)
mask = cv2.imread("./out.png",cv2.IMREAD_UNCHANGED)
cv2.imwrite("input.png", resize(input))
cv2.imwrite("mask.png", resize(mask))
cv2.waitKey(0)
cv2.destroyAllWindows()