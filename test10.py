#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\xtx.png'

img = cv2.imread(file, 0)
cv2.imwrite(save_path+'t.png', img)

#构造矩阵，cv2.MORPH_RECT = np.ones((x, x), np.uint8)
kernel = np.ones((5, 5), np.uint8)
# print(kernel)
#矩形
element = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
#椭圆
# element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
#十字型
# element = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

# print(element)

# 腐蚀
img1 = cv2.erode(img, kernel, iterations = 1)
cv2.imwrite(save_path+'t1.png', img1)

# 膨胀
img2 = cv2.dilate(img, kernel, iterations = 1)
cv2.imwrite(save_path+'t2.png', img2)

# 开运算（先腐蚀再膨胀）（消除椒盐）
img3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite(save_path+'t3.png', img3)

# 闭运算（先膨胀再腐蚀）（消除内部小孔）
img4 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite(save_path+'t4.png', img4)

# 梯度(一幅图膨胀与腐蚀的差别，景象的轮廓)
img5 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite(save_path+'t5.png', img5)

# 礼帽(原始图像与开运算之后的图像的差)
img6 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, element)
cv2.imwrite(save_path+'t6.png', img6)

# 黑帽(闭运算之后的图像与原始图像的差)
img7 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, element)
cv2.imwrite(save_path+'t7.png', img7)


# cv2.namedWindow('image', 0)
# cv2.imshow('image', img1)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
