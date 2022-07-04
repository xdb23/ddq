#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_ms
活动名称: 秒杀
Author: SheYu09
cron: 9 9 * * * jd_ms.py
new Env('秒秒币')
'''
import os
if os.path.exists('jd_jdms.py'):
	os.system('rm -rf jd_jdms.so')
	os.system('mv jd_jdms.py jd_jdms.so')
try:
	from jd_jdms import *
except:
	print('未知错误...')
	exit()

if __name__ == '__main__':
	start()