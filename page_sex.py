#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

import urllib
import urllib.request
from bs4 import BeautifulSoup
import sys
import chardet
import requests
import pathlib


def fun(blocknum,blocksize,totalsize):
    """
    blocknum:当前的块编号
    blocksize:每次传输的块大小
    totalsize:网页文件总大小
    """
    percent = blocknum*blocksize/totalsize
    if percent > 1.0:
        percent = 1.0
    percent = percent*100
    print("download : %.2f%%" %(percent))

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
            print(then)
            try:
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

                        try:
                            resp_code = requests.get(isrc, stream=True).status_code
                            if resp_code == 200:
                                isrclist = isrc.split('.')
                                ilast = '.' + isrclist[-1]
                                now_path = mkpath + str(i) + ilast
                                if pathlib.Path(now_path).exists():
                                    print('this image exist')
                                else:
                                    print(isrc)
                                    urllib.request.urlretrieve(isrc, now_path,fun)
                                i += 1
                        except:
                            print('this image is error')
            except:
                print('makedir error')

def page_url(url):
    req = urllib.request.Request(url=url)
    content = urllib.request.urlopen(req).read()
    typeEncode = sys.getfilesystemencoding()
    infoencode = chardet.detect(content).get('encoding', 'utf-8')
    html = content.decode(infoencode, 'ignore').encode(typeEncode)

    soup = BeautifulSoup(html, 'html.parser')
    span_soup = soup.select('span[id="fd_page_bottom"]')
    page_soup = BeautifulSoup('<html><body>' + str(span_soup[0]) + '</body></html>', 'html.parser')
    page_a = page_soup.select('a[href*=".html"]')
    num = 0;
    pre_str = ''
    for a in page_a:
        val = a.get_text()
        if '... ' in val:
            num = int(val.strip('... '))
            href_str = a.attrs['href']
            pre_str = href_str.strip(str(num)+'.html')
    for item in range(num+1):
        if item > 4:
            url_then = 'http://www.hxsq62.com/'+pre_str+str(item)+'.html'
            print(url_then)
            path = 'E:\spider\\'
            download(url_then,path)
url = 'http://www.hxsq62.com/forum-56-1.html'
page_url(url)