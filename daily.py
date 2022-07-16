#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_daily
活动名称: 天天优惠大乐透, 哲学系
Author: SheYu09
cron: 7 9 * * * jd_daily.py
new Env('天天领奖')
'''
import os
if os.path.exists('jd_daily.py'):
	os.system('rm -rf jd_daily.so')
	os.system('mv jd_daily.py jd_daily.so')
try:
	from jd_daily import start
except:
	print('未知错误...')
	exit()

if __name__ == '__main__':
	start()