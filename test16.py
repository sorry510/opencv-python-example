#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file_path = 'D:\\opencv\\exam_imagick\\images\\'

img = cv2.imread(file_path+'page1.png')
img1 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, 3)
cv2.imwrite(save_path+'t.png', edges)

# 霍夫变换
#（1,2,3,4）(img(二值化),ρ精度,θ精度,阀值(直线最短长度px))返回ρ（原点到直线的垂直距离），θ弧度（p与横轴顺时针的夹角）
lines = cv2.HoughLines(edges, 1, np.pi/180, 800)
for line in lines:
	# print(line[0][0], line[0][1])
	for rho, theta in line:
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a * rho
		y0 = b * rho
		x1 = int(x0 + 1000 * (-b))
		y1 = int(y0 + 1000 * (a))
		x2 = int(x0 - 1000 * (-b))
		y2 = int(y0 - 1000 * (-a))

		cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imwrite(save_path+'t1.png', img)

# 霍夫变换改进方法
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 400, minLineLength, maxLineGap)

for line in lines:
	for x1, y1, x2, y2 in line:
		cv2.line(img1, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite(save_path+'t2.png', img1)





# cv2.namedWindow('image', 0)
# cv2.imshow('image', img2)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
