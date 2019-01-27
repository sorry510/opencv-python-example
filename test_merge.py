#! /usr/bin/env python
# !-*- codding:utf-8 -*-
import sys
import cv2
import numpy as np

path1, path2 = sys.argv[-2:]


img1 = cv2.imread(path1)
h1, w1 = img1.shape[:2]
img2 = cv2.imread(path2)
h2, w2 = img2.shape[:2]

newImg = np.zeros((h1+h2, w1, 3), dtype = np.uint8)
newImg[0:h1, :] = img1
newImg[h1:, :] = img2

cv2.imwrite('merge.jpg', newImg)

# cv2.namedWindow('image', 0)
# cv2.imshow('image', newImg)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()