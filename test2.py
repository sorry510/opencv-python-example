#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2


save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'

#图片的鼠标事件，27键位是esc
def drawCircle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img, (x,y), 100, (255, 0, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', drawCircle)

while True:
	cv2.imshow('image', img)
	if cv2.waitKey(20) & 0xFF == 27:
		break
cv2.destroyAllWindows()

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

