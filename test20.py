#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

# 写文字
save_path = './imgs/'

img = cv2.imread(save_path + 'blank.png')

cv2.putText(img, "01234567890A123", (300,300), cv2.FONT_HERSHEY_PLAIN , 2, (0,0,255), 2)

cv2.imwrite(save_path+'test/num.jpg', img)


cv2.namedWindow('image', 0)
cv2.imshow('image', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
