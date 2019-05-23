#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

import urllib.request as urllib

opener = urllib.OpenerDirector()

i = 0
j = 1
for row in open('G:\\images\\raw_data\\porn\\urls_porn.txt'):
    try:
        url = row.strip()
        print(url)
        print('count : ' + str(j))
        j += 1
        # 避免无效连接，设置超时时间，单位为秒
        opener.open(url , data=None, timeout=0.01)
        path = 'E:\\row_data\\' + str(i) + '.jpg'
        urllib.urlretrieve(url, path)
        i += 1
        print('save : ' + str(i))
    except Exception as e:
        print('get and download error',e)