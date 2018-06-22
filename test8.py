#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\2.jpg'

img = cv2.imread(file)
h, w = img.shape[:2]
print(h, w)#332, 500

#图像放仿射变换(构建一个2X3矩阵(原图3点和仿射后3点))
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
img1 = cv2.warpAffine(img, M, (w, h))

#旋转getRotationMatrix2D(旋转中心，角度， 缩放因子)
M = cv2.getRotationMatrix2D((w/2, h/2), 45, 1.)
img2 = cv2.warpAffine(img, M, (w, h))

# 透视变换(构建一个3X3矩阵(原图4点和透视后4点))
pts1 = np.float32([[50, 20], [450, 20], [50, 280], [450, 280]])
pts2 = np.float32([[0, 0], [400, 0], [0, 250], [400, 250]])
M = cv2.getPerspectiveTransform(pts1, pts2)
img3 = cv2.warpPerspective(img, M, (400, 250))

cv2.imwrite(save_path+'t.png', img)
cv2.imwrite(save_path+'t1.png', img1)
cv2.imwrite(save_path+'t2.png', img2)
cv2.imwrite(save_path+'t3.png', img3)

# cv2.namedWindow('image3', 0)
# cv2.imshow('image3', img3)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
