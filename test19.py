#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2
import math

file_path = 'imgs/'

img1 = cv2.imread(file_path+'t1.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

def paper_split(self, path):
      try:
          img = np.array(cv.imread(path))
          shape = img.shape
          center = int(shape[0] / 2) + 1
          page1 = img[0:center, :]
          page2 = img[center:, :]
          return (page1, page2)

      except Exception as ex:
          print("error：", ex.message)
          print('not find img')
          return None

def get_ret(f):
	img2 = cv2.imread(file_path+f)
	gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	#灰度图的相似度
	ret = cv2.matchShapes(gray1, gray2, 1, 0.0)
	print(ret)


def cardRotate(img, angle=180):
	rows,cols,channels = img.shape
	M = cv2.getRotationMatrix2D((cols/2,rows/2), angle, 1)
	img = cv2.warpAffine(img, M, (cols,rows), borderValue=(255, 255, 255))#旋转后空余部分填充白色
	return img



def rotate_about_center(f, angle=180, scale=1.):
	src = cv2.imread(file_path+f)
	w = src.shape[1]
	h = src.shape[0]
	rangle = np.deg2rad(angle)  # angle in radians
	# now calculate new image width and height
	nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
	nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
	# ask OpenCV for the rotation matrix
	# ask OpenCV for the rotation matrix
	rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
	# calculate the move from the old center to the new center combined
	# with the rotation
	rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5,0]))
	# the move only affects the translation, so update the translation
	# part of the transform
	rot_mat[0,2] += rot_move[0]
	rot_mat[1,2] += rot_move[1]
	img2 =  cv2.warpAffine(src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), borderValue=(255, 255, 255))
	gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	#灰度图的相似度
	ret = cv2.matchShapes(gray1, gray2, 1, 0.0)
	print(ret)



get_ret('t1-1.jpg')
# get_ret('t2.jpg')
get_ret('t2-1.jpg')
# get_ret('t3.jpg')
# get_ret('test1.jpg')

# print(cv2.CONTOURS_MATCH_I1)
# print(cv2.CONTOURS_MATCH_I2)
# print(cv2.CONTOURS_MATCH_I3)


# rotate_about_center('t1-1.jpg')



