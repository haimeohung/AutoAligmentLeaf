# AutoAligmentLeaf
Tìm contour, trong AutoAlgment -> detect symmetry, trong hàm auto_rotate, dòng contour = max(contours, key = cv2.contourArea) là contour to nhất bao quanh object. Muốn lấy thằng này, sửa lại thành:
return img_rgb, drawing, ellipse[2], contour
Chỗ trả về sửa lại thành:
img_rgb, drawing, corner, contour = auto_rotate(img)
Thực thi: trong terminal gõ tên file là tự chạy
Package: opencv-contrib
         opencv
         matplotlib
         numpy
