# ! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

import urllib
import urllib.request
from bs4 import BeautifulSoup
import sys
import chardet


def download(url):
    req = urllib.request.Request(url)
    content = urllib.request.urlopen(req).read()
    typeEncode = sys.getfilesystemencoding()
    infoencode = chardet.detect(content).get('encoding', 'utf-8')
    html = content.decode(infoencode, 'ignore').encode(typeEncode)
    soup = BeautifulSoup(html, 'html.parser')
    span = soup.select('h1 > span')
    if len(span) == 1:
        title = span[0].getText()
    else:
        title = '404'
    return title


url_head = 'https://mini.eastday.com/a/'
url_bottom = '.html'

# bb = open('G:\images\\008_2.txt', 'w')
csv_path = 'G:\images\\sample_url_8.txt'
index = 1
path_url=[]
with open(csv_path, 'r', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        url = url_head + line + url_bottom
        path_url.append(url)

f.close()

for url in path_url:
    res = download(url)
    print(url + ',' + res)
#     print(res)
#     bb.write(url)
#     bb.write(',')
#     try:
#         bb.write(res)
#     except:
#         bb.write('404')
#     bb.write('\n')
#     index = index + 1
#     bb.flush()
# bb.close()

