#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2

save_path = 'D:\\opencv\\exam_imagick\\images\\test\\'
file = 'D:\\opencv\\exam_imagick\\images\\2.jpg'

img = cv2.imread(file)
img1 = img.copy()

#创造一个和原图大小一样但全是0的灰度图
zeros = np.zeros(img.shape[:2], dtype = "uint8")

#拆分合并通道
# b, g, r = cv2.split(img1)#操作费时不推荐
b = img1[:, :, 0]
g = img1[:, :, 1]
r = img1[:, :, 2]

#混合2张图片（img1权重0.7，img2权重0.3，可能需要2图大小相同，类型一致，没有测试）
#cv2.addWeighted(img1, 0.7, img2, 0.3, 0)


# img2 = cv2.merge([b, zeros, zeros])
# cv2.imwrite(save_path+'b-zeros.png', img2)
# img2 = cv2.merge([zeros, g, zeros])
# cv2.imwrite(save_path+'g-zeros.png', img2)
# img2 = cv2.merge([zeros, zeros, r])
# cv2.imwrite(save_path+'r-zeros.png', img2)

# img2 = cv2.merge([g, b, r])
# img2 = cv2.merge([r, g, b])
# img2 = cv2.merge([b, r, g])

# cv2.imwrite(save_path+'b.png', b)
# cv2.imwrite(save_path+'g.png', g)
# cv2.imwrite(save_path+'r.png', r)

# cv2.namedWindow('image', 0)
# cv2.imshow('image', img2)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()
