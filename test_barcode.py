#!/usr/bin/python
# -*- coding:utf-8 -*-
import cv2  
import numpy as np

save_path = 'imgs/test/'
file = 'imgs/test.png'

img = cv2.imread(file)

# img = img[1830:1860, 2110:2330] #second positive
# img = img[1660:1695, 130:350] #first negative
h, w = img.shape[:2]

# cv2.namedWindow('image', 0)
# cv2.imshow('image', img)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
# exit()

cv2.imwrite(save_path+'t.png', img)

#缩放
img2 = cv2.resize(img, (w * 2, h * 2), interpolation=cv2.INTER_CUBIC)
cv2.imwrite(save_path+'t1.png', img2)

img3 = cv2.blur(img,(3, 3))
cv2.imwrite(save_path+'t3.png', img3)

img4 = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imwrite(save_path+'t4.png', img4)

#二值化
img5 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, img5 = cv2.threshold(img5, 200, 255, cv2.THRESH_BINARY)
cv2.imwrite(save_path+'t5.png', img5)
  
# x = cv2.Sobel(img,cv2.CV_16S,1,0)  
# y = cv2.Sobel(img,cv2.CV_16S,0,1)  
  
# absX = cv2.convertScaleAbs(x)
# absY = cv2.convertScaleAbs(y)  
  
# dst = cv2.addWeighted(absX,0.5,absY,0.5,0)
# cv2.imwrite(save_path+'ttt.png', dst)  
  
