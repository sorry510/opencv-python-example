#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = './imgs/test/'
file_path = './imgs/'

imgy = cv2.imread(file_path+'number.jpg')
img = cv2.cvtColor(imgy, cv2.COLOR_BGR2GRAY)
# cv2.imwrite(save_path+'t.png', img)
img1 = img.copy()

img2 = cv2.imread(file_path+'child.png')
h, w = img2.shape[:2]
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# cv2.imwrite(save_path+'tt.png', img2)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# methods = ['cv2.TM_CCOEFF_NORMED']
k = 0
for meth in methods:
	img = img1.copy()
	method = eval(meth)

	res = cv2.matchTemplate(img, img2, method)

	# method1 适用于cv2.TM_CCOEFF_NORMED，可以根据阀值找到多个匹配图像
	# threshold = 0.6
	# loc = np.where(res >= threshold)
	# for pt in zip(*loc[::-1]):
	# 	cv2.rectangle(imgy, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)

	# method2，6中方法
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(imgy, top_left, bottom_right, 255, 2)

	cv2.imwrite(save_path+'t'+str(k)+'.png', imgy)
	k += 1




# cv2.namedWindow('image', 0)
# cv2.imshow('image', img2)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
