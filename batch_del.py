import os

# 批量删除空文件夹

spath = 'E:\spider'
paths = os.listdir(spath)
for pa in paths:
    filepath = os.path.join(spath,pa)
    if not os.listdir(filepath):
        print(filepath)
