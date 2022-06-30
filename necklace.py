#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / necklace
活动名称: 点点卷
Author: SheYu09
cron: 7 9 * * * necklace.py
new Env('点点卷')
'''
import os
if os.path.exists('jd_necklace.py'):
	os.system('rm -rf jd_necklace.so')
	os.system('mv jd_necklace.py jd_necklace.so')
try:
	from jd_necklace import *
except:
	print('未知错误...')
	exit()

if __name__ == '__main__':
	start()