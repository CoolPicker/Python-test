#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

import urllib
import urllib.request
from bs4 import BeautifulSoup
import sys
import chardet
import requests


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
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(req).read()
    typeEncode = sys.getfilesystemencoding()
    infoencode = chardet.detect(content).get('encoding', 'utf-8')
    html = content.decode(infoencode, 'ignore').encode(typeEncode)

    soup = BeautifulSoup(html,'html.parser')

    # 第一页处理
    form1 = soup.select('ul[id="waterfall"]')

    soup2 = BeautifulSoup('<html><body>' + str(form1[0]) + '</body></html>', 'html.parser')
    a_url = soup2.select('a[href*=".html"]')
    for a in a_url:
        val = a.get_text()
        then = val.strip()
        if then!='' and then != 'admin':
            # print(then) 创建文件夹
            mkpath = path + then + "\\"
            mkdir(mkpath)
            href = a.attrs['href']
            href = 'http://www.hxsq62.com/' + href
            # print(href) 帖子url
            req = urllib.request.Request(url=href, headers=headers)
            content = urllib.request.urlopen(req).read()
            typeEncode = sys.getfilesystemencoding()
            infoencode = chardet.detect(content).get('encoding', 'utf-8')
            html = content.decode(infoencode, 'ignore').encode(typeEncode)
            td_soup = BeautifulSoup(html, 'html.parser')
            td_image = td_soup.select('td[class="t_f"]')
            image_soup = BeautifulSoup('<html><body>' + str(td_image[0]) + '</body></html>', 'html.parser')
            img_label = image_soup.select('img')
            i = 0
            for label in img_label:
                if label.has_attr('file'):
                    isrc = label.attrs['file']
                    print(isrc)
                    try:
                        resp_code = requests.get(isrc, stream=True).status_code
                        if resp_code == 200:
                            isrclist = isrc.split('.')
                            ilast = '.' + isrclist[-1]
                            urllib.request.urlretrieve(isrc, mkpath + str(i) + ilast)
                            i += 1
                    except:
                        print('this image is error')
def page_url(url):
    req = urllib.request.Request(url=url)
    content = urllib.request.urlopen(req).read()
    typeEncode = sys.getfilesystemencoding()
    infoencode = chardet.detect(content).get('encoding', 'utf-8')
    html = content.decode(infoencode, 'ignore').encode(typeEncode)

    soup = BeautifulSoup(html, 'html.parser')


url = 'http://www.hxsq62.com/forum-56-1.html'
path = 'E:\spider\\'
download(url,path)




# 定义要创建的目录
# mkpath = "/home/han/niuya/image/tom/"
# 调用函数
# mkdir(mkpath)