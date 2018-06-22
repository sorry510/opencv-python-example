#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\2.jpg'

img = cv2.imread(file)

#边缘检测
#Canny(1, 2, 3, 4, 5) 1:img, 2:minVal, 3:maxVal, 4:Sobel卷积核大小，默认3, 5:默认False, 设定求梯度大小的方程
img1 = cv2.Canny(img, 100, 200)
cv2.imwrite(save_path+'t1.png', img1)


# cv2.namedWindow('image', 0)
# cv2.imshow('image', img2)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
