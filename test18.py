#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file_path = 'D:\\opencv\\exam_imagick\\images\\'

#图像物体分割，分水岭算法
img = cv2.imread(file_path+'barcode.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(save_path+'t1.png', gray)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
cv2.imwrite(save_path+'t2.png', thresh)
