#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jdms
活动名称: 秒杀
Author: SheYu09
cron: 7 9 * * * jdms.py
new Env('秒秒币')
'''
import os
if os.path.exists('jd_jdms.py'):
	os.system('rm -rf jd_jdms.so')
	os.system('mv jd_jdms.py jd_jdms.so')
try:
	from jd_jdms import start
except:
	print('未知错误...')
	exit()

if __name__ == '__main__':
	start()