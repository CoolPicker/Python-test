#!/usr/bin/python3
# -*- coding:utf8 -*-

import imghdr
import urllib.request

path = 'G:\images\\used\\'
csv_path = 'G:\images\\robot1.csv'
f = open('G:\images\\check_error.txt', 'wb')

data = []
error_images = []
with open(csv_path, 'r', encoding="utf-8") as f:
    header = f.readline().split(',')
    counter = 0
    for line in f:
        try:
            fields = line.split(",")
            name = fields[0]
            url = fields[2]
            local_path = path + name + '.jpg'
            print(url.strip())
            print(local_path)
            urllib.request.urlretrieve(url, local_path)
            check = imghdr.what(local_path)
            if check == None:
                f.write(name)
                f.write(',')
                f.write(url)
                f.write(',')
                f.write(local_path)
                f.write('\n')
                error_images.append(url)
        except:
            print(line)
        print(counter)
        counter = counter + 1
print(counter)
print(error_images)