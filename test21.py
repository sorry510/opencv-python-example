#! /usr/bin/env python
# -*- coding:utf-8 -*-

import cv2
import numpy as np
import pytesseract
import pymysql

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract'

def checkImg(img):
	img = cv2.imread(img, 0)
	img = cv2.GaussianBlur(img, (5, 5), 0)
	# kernel = np.ones((3, 3), np.uint8)
	# element = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
	# img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	# img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	# img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, element)
	# img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, element)
	cv2.namedWindow('image', 0)
	cv2.imshow('image', img)
	cv2.waitKey(0) & 0xFF
	cv2.destroyAllWindows()

	strout = pytesseract.image_to_string(img)
	print(strout)
	arr = strout.split('A')
	code = qid = None
	if len(arr) == 2:
		for val in arr:
			val = trim(val)
			if len(val) >= 10:
				code = val[len(val)-10:]
			else:
				qid = int(val)
	else:
		print('识别失败')

	print('code,qid', code, qid)
	exit()
	# if code and qid:
	# 	sql = "select id from student_paper_detail where student_id = (select id from student where code = %s) and question_id = %d"
	# 	res = doSql(sql,(code, qid))
	# 	if res:
	# 		# 更新
	# 		print('没问题')
	# 	else:
	# 		# 更新
	# 		print('图片错误')
	# else:
	# 	print('识别失败')


def doSql(sql, data):
	conn = pymysql.connect(host='dev.gammainfo.com', port='3306', user='root', passwd='Gamma_201809', db='as_test_percent', charset='utf8')
	cursor = conn.cursor()
	effect_row = cursor.execute(sql, data)
	rows = cursor.fetchone()
	conn.commit()
	cursor.close()
	return rows

def trim(string):
	return ''.join([i for i in string if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']])

if __name__ == '__main__':
	checkImg('imgs/page_207.png')