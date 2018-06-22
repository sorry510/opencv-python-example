#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2


save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'

imgs = []
img = np.zeros((512,512,3), np.uint8)
imgs.append(img)

#在图片上面化线条，矩形，圆形，-1代表实体，>0代表空心
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()
img4 = img.copy()
img5 = img.copy()
img6 = img.copy()

img1 = cv2.line(img1, (0, 0), (511, 511), (255, 0, 0), 5)#化线会在原图上修改(img, left top, right bottom, color, widths)
imgs.append(img1)

img2 = cv2.rectangle(img2, (12, 34), (223, 332), (0, 255, 0), 2)#化线会在原图上修改(img, left top, right bottom, color, widths)
imgs.append(img2)

img3 = cv2.circle(img3, (250, 250), 60, (0, 0, 255), -1)#化线会在原图上修改(img, left top, right bottom, color, widths)
imgs.append(img3)

img4 = cv2.circle(img4, (250, 250), 60, (255, 255, 255), 2)#化线会在原图上修改(img, left top, right bottom, color, widths)
imgs.append(img4)


k = 0
for img in imgs:
	cv2.imwrite(save_path + 'test_' + str(k) + '.png', img)
	k += 1