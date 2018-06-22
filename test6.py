#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\2.jpg'

#取颜色阀之
g = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(g, cv2.COLOR_BGR2HSV)
print(hsv_green)

# cv2.namedWindow('image', 0)
# cv2.imshow('image', img2)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
