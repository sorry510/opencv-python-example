#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\code\\2018-05-17-11-11-14-5afcf2d2c009a.jpg'

img = cv2.imread(file)

img = img[1835:1855, 2125:2330]
h, w = img.shape[:2]
#图像缩放
img2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
img3 = cv2.resize(img, (w / 2, h / 2), interpolation=cv2.INTER_CUBIC)

# cv2.imwrite(save_path+'t1.png', img)
# cv2.imwrite(save_path+'t2.png', img2)
# cv2.imwrite(save_path+'t3.png', img3)

# cv2.namedWindow('image', 0)
# cv2.imshow('image', img)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
