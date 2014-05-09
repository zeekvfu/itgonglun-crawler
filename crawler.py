#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# crawler.py


import sys
import logging
import re
import urllib.request
import urllib.error

import multi_thread_continous_download
from multi_thread_continous_download import multi_thread_continous_download


# 解析 HTML 代码，得到下载链接
def parse_download_url(index, regex):
	index_url = ""
	if (index == 58):
		index_url = "http://www.itgonglun.com/episodes/59-1"
	else:
		index_url = "http://www.itgonglun.com/episodes/" + str(index)
	try:
		with urllib.request.urlopen(index_url) as response:
			# print(response.status, response.reason)
			if (response.status != 200):
				return
			text = response.read().decode('utf-8')
			# print(text)
			url_list = regex.findall(text)
			count = len(url_list)
			if (count != 1):
				print("parse_download_url(): regular expression match count %d !" %(count))
				return
			end_pos = url_list[0].find(".mp3");
			if (end_pos == -1):
				print("parse_download_url(): file type not mp3!")
			return url_list[0][10:end_pos+4]
	except urllib.error.URLError as e:
		print(e.errno, '\n', e.reason, '\n')
		return


print('将从「IT 公论」（http://www.itgonglun.com/）下载 podcast episodes ...')
begin = int(input('请输入开始的期数：'))
end   = int(input('请输入结束的期数：'))

# data-url="http://traffic.libsyn.com/itgonglun/IT__ep1_-_iPad_Air_iPad_mini_2_Mavericks_GM.mp3"
rule = "data-url=\"http://traffic\.libsyn\.com/itgonglun/IT__ep\d+_-_.*\.mp3\s*\""
regex = re.compile(rule)

log_file = 'url.log'
with open(log_file, 'at') as logger:
	logger.write('\n****************************************************************************************************\n')

# 写日志到文件
logging.basicConfig(filename=log_file, format="%(asctime)s,%(msecs)d\t%(levelname)s\t%(message)s", datefmt="%Y-%m-%d %H:%M:%S", style='%', level=logging.DEBUG)
# 写日志到 stdout
stdout_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(fmt="%(asctime)s,%(msecs)d\t%(levelname)s\t%(message)s", datefmt="%Y-%m-%d %H:%M:%S", style='%')
stdout_handler.setFormatter(formatter)
logging.getLogger().addHandler(stdout_handler)

for index in range(begin, end+1):
	url = parse_download_url(index, regex)
	if url is None:
		continue
	logging.info(str(index) + '\t' + url)
	multi_thread_continous_download(url)

logging.shutdown()




# 比较特殊的 URL：
# 58			http://www.itgonglun.com/episodes/59-1




