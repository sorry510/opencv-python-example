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
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imwrite(save_path+'t2.png', thresh)
kernel = np.ones((2,2), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)
cv2.imwrite(save_path+'t3.png', opening)
sure_bg = cv2.dilate(opening, kernel, iterations = 3)
cv2.imwrite(save_path+'t4.png', sure_bg)
dist_transform = cv2.distanceTransform(opening, 1, 5)
cv2.imwrite(save_path+'t5.png', dist_transform)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
cv2.imwrite(save_path+'t6.png', sure_fg)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
cv2.imwrite(save_path+'t7.png', unknown)