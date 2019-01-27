#! /usr/bin/env python
# !-*- codding:utf-8 -*-

import cv2
import numpy as np
import random

color = lambda x, y: int(x + random.random() * (y-x))
arr = lambda num: [color(0, 255) for x in range(num)]
w = 500
h = 300
img = np.array(arr(w * h * 3)).reshape(h, w, 3)  
cv2.imwrite('random.png', img)

# cv2.namedWindow('image', 1)
# cv2.imshow('image', img)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()