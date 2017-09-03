#coding=utf-8
#os.walk()
#获取每个文件的绝对路径,不包含目录
import os
g = os.walk('D:/linyouwei/python/testdir')

for path,d,filelist in g:
    for f in filelist:
        print os.path.join(path,f)


