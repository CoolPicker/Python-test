#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

import urllib
import urllib.request
from bs4 import BeautifulSoup
import sys
import chardet
# import urllib
import re


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 / 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        os.makedirs(path)
        # print path + ' 创建成功'
        return True
    else:
        # print path + ' 目录已存在'
        return False

def download(url,path):
    req = urllib.request.Request(url)
    content = urllib.request.urlopen(req).read()
    typeEncode = sys.getfilesystemencoding()
    infoencode = chardet.detect(content).get('encoding', 'utf-8')
    html = content.decode(infoencode, 'ignore').encode(typeEncode)

    soup = BeautifulSoup(html,'html.parser')
    a_url = soup.select('a[href*=".shtml"]')

    z = 0

    n = 0
    for a in a_url:
        href = a.attrs['href']
        val = a.get_text()
        then = val.strip()
        if then != '':
            print(then)
            req = urllib.request.Request(href)
            content = urllib.request.urlopen(req).read()
            typeEncode = sys.getfilesystemencoding()
            infoencode = chardet.detect(content).get('encoding', 'utf-8')
            html = content.decode(infoencode, 'ignore').encode(typeEncode)
            thensoup = BeautifulSoup(html,'html.parser')
            thenimgs_url = thensoup.select('div[class="left"]')

            # urlTT = href
            # pathTT = '/home/han/niuya/image/'
            # download(urlTT, pathTT)
            if len(thenimgs_url)!=0:
                souptest = BeautifulSoup('<html><body>'+str(thenimgs_url[0])+'</body></html>','html.parser')
                testimgs_url = souptest.select('div[id="artical"]')
                if len(testimgs_url) != 0:
                    souptest = BeautifulSoup('<html><body>' + str(testimgs_url[0]) + '</body></html>', 'html.parser')
                    thenimgs_url = souptest.select('img')
                    i = 0
                    j = 0
                    for iurl in thenimgs_url:
                        if iurl.has_attr('src'):
                            isrc = iurl.attrs['src']
                            if isrc != "":
                                mkpath = path + then + "\\"
                                boolmk = mkdir(mkpath)
                                pattern = re.compile(r'.*2018.*')
                                match = pattern.match(isrc)
                                if match:
                                    isrclist = isrc.split('.')
                                    ilast = '.' + isrclist[-1]
                                    urllib.request.urlretrieve(isrc, mkpath + str(j) + ilast)
                                    print(isrc)
                                    j += 1
                        i += 1
        n += 1

    imgs_url = soup.select('img')
    m = 0
    for url in imgs_url:
        src = url.attrs['src']
        print(src)
        srclist = src.split('.')
        last = '.'+srclist[-1]
        urllib.urlretrieve(src, path + str(z) + last)
        m += 1
        z += 1
    print
    'download complete'

url = 'http://www.ifeng.com/'
path = 'E:\spider\\'
download(url,path)




# 定义要创建的目录
# mkpath = "/home/han/niuya/image/tom/"
# 调用函数
# mkdir(mkpath)