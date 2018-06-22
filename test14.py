#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\2.jpg'

img = cv2.imread(file)
cv2.imwrite(save_path+'t.png', img)

#灰度图
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(save_path+'t1.png', img1)

#二值化
ret, img2 = cv2.threshold(img1, 127, 255, 0)
cv2.imwrite(save_path+'t2.png', img2)

#找轮廓
img2, contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#画轮廓1:img, 2:轮廓, 3:轮廓索引（-1为全部），4：颜色，5：厚度
img3 = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
cv2.imwrite(save_path+'t4.png', img3)

cnt = contours[54]
cnt2 = contours[55]
#返回轮廓的一个字典信息
M = cv2.moments(cnt)
# print(M)

#轮廓的重心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
#轮廓的面积
area = M['m00']
area = cv2.contourArea(cnt)
#轮廓的周长
perimeter = cv2.arcLength(cnt, True)#true指定对象的形状是闭合，false是打开的（一条曲线）

#轮廓近似
# epsilon	= 0.1 * cv2.arcLength(cnt, True)#原始轮廓到近似轮廓的最大距离,这个值自行调整，影响慎重
# approx = cv2.approxPolyDP(cnt, epsilon, True)

#轮廓方向
# (x, y), (MA, ma), angle = cv2.fitELLipse(cnt)

#轮廓的极点
# leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
# rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
# topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
# bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

#点到对象轮廓的最短距离(点在轮廓外，返回值为负，上面为0，内部为正，第三个参数为True，返回距离，为false只返回位置关系（-1,0,1）)
dist = cv2.pointPolygonTest(cnt, (50,50), True)

#形状匹配，比较2个形状或轮廓的相似程度，返回值越小，匹配越好
ret = cv2.matchShapes(cnt, cnt2, 1, 0.0)

print(dist, ret)


# cv2.namedWindow('image', 0)
# cv2.imshow('image', img2)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
