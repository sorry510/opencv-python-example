#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\test.png'


#基本读写图片
img = cv2.imread(file)
cv2.namedWindow('image', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite(save_path+'1.png', img)
    cv2.destroyAllWindows()




