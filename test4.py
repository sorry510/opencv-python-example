#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\test.png'

img = cv2.imread(file)
print(img.shape)
print(img.size)
print(img.dtype)

img1 = img.copy()
block = img1[150:350, 600:1100]

#复制一块到一个地方
img1[500:700, 1500:2000] = block
block2 = img1[500:700, 1500:2000]

cv2.namedWindow('image', 0)
cv2.imshow('image', img1)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
