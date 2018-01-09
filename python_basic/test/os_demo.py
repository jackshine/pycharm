#coding=utf-8
#遍历文件目录
import  os
a=[]
def dirList(path):
    list = os.listdir(path)
    for b in list:
        filepath = path + "/" + b
        if os.path.isdir(filepath):
            dirList(filepath)
        a.append(filepath)
    return  a
print dirList("D:/linyouwei/python/testdir")