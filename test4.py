#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'imgs/test1.jpg'

img = cv2.imread(file)
# (x,y,w,h)
img2 = cv2.getRectSubPix(img, (300,500), (100,1000))
# print(img2)
# exit()

# print(img.shape)
# print(img.size)
# print(img.dtype)

# img1 = img.copy()
# block = img1[150:350, 600:1100]

# #复制一块到一个地方
# img1[500:700, 1500:2000] = block
# block2 = img1[500:700, 1500:2000]

cv2.namedWindow('image', 0)
cv2.imshow('image', img2)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
