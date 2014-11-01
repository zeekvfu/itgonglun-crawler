#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# crawler.py


import sys, re
import logging
import urllib.request, urllib.error

import multi_thread_continous_download
from multi_thread_continous_download import multi_thread_continous_download




# 获取 URL 下载链接
def get_download_url(index):
	url = ''
	# 「IT 公论」没有第 70 期
	if index == 70:
		url = None
	else:
		url = 'http://ipn.li/itgonglun/' + str(index) + '/audio.mp3'
	return url


print('将从「IT 公论」（http://ipn.li/itgonglun/）下载 podcast episodes ...')
begin = int(input('请输入开始的期数：'))
end   = int(input('请输入结束的期数：'))

log_file = 'url.log'
with open(log_file, 'at') as logger:
	logger.write('\n*********************************************************************************************************\n')

# 写日志到文件
logging.basicConfig(filename=log_file, format="%(asctime)s,%(msecs)d\t%(levelname)s\t%(message)s", datefmt="%Y-%m-%d %H:%M:%S", style='%', level=logging.DEBUG)
# 写日志到 stdout
stdout_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(fmt="%(asctime)s,%(msecs)d\t%(levelname)s\t%(message)s", datefmt="%Y-%m-%d %H:%M:%S", style='%')
stdout_handler.setFormatter(formatter)
logging.getLogger().addHandler(stdout_handler)

for index in range(begin, end+1):
	url = get_download_url(index)
	if url is not None:
		logging.info(str(index) + '\t' + url)
		multi_thread_continous_download(url, str(index) + '.mp3')

logging.shutdown()




# 比较特殊的下载链接：
# 70		无




