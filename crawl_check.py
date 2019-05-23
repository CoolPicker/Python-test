
#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

import urllib
import urllib.request
from bs4 import BeautifulSoup
import sys
import chardet


def download(url, path):
    req = urllib.request.Request(url)
    content = urllib.request.urlopen(req).read()
    typeEncode = sys.getfilesystemencoding()
    infoencode = chardet.detect(content).get('encoding', 'utf-8')
    html = content.decode(infoencode, 'ignore').encode(typeEncode)

    soup = BeautifulSoup(html, 'html.parser')
    table_tr = soup.select('h1 > span')
    print(len(table_tr))
    index = 0
    for tr_td in table_tr:
        if index > 0:
            td_index=0
            name = ''
            url = ''
            for td in tr_td.findAll('td'):
                # print(td)
                if td_index==0:
                    name=td.getText()
                if td_index==4:
                    url=td.getText()
                td_index = td_index + 1
            local_path = path + name
            print(url)
            urllib.request.urlretrieve(url, local_path)
        index = index + 1

url = 'http://autocenter.mop.com/mopauto/Robot/show?p=1'
path = 'G:\images\\used\\'
download(url, path)