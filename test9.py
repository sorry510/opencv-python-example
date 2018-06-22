#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\2.jpg'

img = cv2.imread(file)

#2D卷积
kernel = np.ones((5, 5), np.float32) / 25
img1 = cv2.filter2D(img, -1 , kernel)
cv2.imwrite(save_path+'t1.png', img1)

#平均
img2 = cv2.blur(img, (5, 5))
cv2.imwrite(save_path+'t2.png', img2)

#高斯(必须奇数)
img3 = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite(save_path+'t3.png', img3)

#中值(必须奇数)
img4 = cv2.medianBlur(img, 5)
cv2.imwrite(save_path+'t4.png', img4)

#双边滤波(9邻域直径，两个75分别是空间高斯函数标准差，灰度值相似性高斯函数标准差)
img5 = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imwrite(save_path+'t5.png', img5)
# cv2.namedWindow('image', 0)
# cv2.imshow('image', img2)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
