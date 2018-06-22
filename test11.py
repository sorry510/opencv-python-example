#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\2.jpg'

img = cv2.imread(file)

#梯度滤波器

#拉普拉斯算子,cv2.CV_64F 输出图像的深度，可使用-1 与原图像保持一致
img1 = cv2.Laplacian(img, cv2.CV_64F)
cv2.imwrite(save_path+'t1.png', img1)

img2 = cv2.Laplacian(img, -1)
cv2.imwrite(save_path+'t2.png', img2)

#参数1,0 为只在x方向求一介导数， 最大可以求2介导数
img3 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
cv2.imwrite(save_path+'t3.png', img3)

#参数0,1 为只在y方向求一介导数， 最大可以求2介导数
img4 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)
cv2.imwrite(save_path+'t4.png', img4)

#修正位数
img5 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
img5 = np.absolute(img5)
img5 = np.uint8(img5)
cv2.imwrite(save_path+'t5.png', img5)



print(cv2.CV_64F)

# cv2.imwrite(save_path+'t4.png', img4)

# cv2.namedWindow('image', 0)
# cv2.imshow('image', img2)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
