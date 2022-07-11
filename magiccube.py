#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / magiccube
活动名称: 集魔方
Author: SheYu09
cron: 7 9 * * * magiccube.py
new Env('集魔方')
'''
import os
if os.path.exists('jd_magiccube.py'):
	os.system('rm -rf jd_magiccube.so')
	os.system('mv jd_magiccube.py jd_magiccube.so')
try:
	from jd_magiccube import start
except:
	print('未知错误...')
	exit()

if __name__ == '__main__':
	start()