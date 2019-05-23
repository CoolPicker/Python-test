#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

import urllib.request as urllib
import time
import datetime


opener = urllib.OpenerDirector()



print('%.20f' % time.time())

url = 'https://ci.phncdn.com/pics/albums/013/889/491/173801711/(m=e-yaaGqaa)(mh=keF16B9jroWqJNLf)original_173801711.jpg'
try:
    opener.open(url,timeout=0.01)
    print('23242')
    print('%.20f' % time.time())
    urllib.urlretrieve(url, 'E:\\row_data\\' + str(1) + '.jpg')
except Exception as e:
    print(e)
opener.open(url)
urllib.urlretrieve(url, 'E:\\row_data\\' + str(1) + '.jpg')
print('%.20f' % time.time())
