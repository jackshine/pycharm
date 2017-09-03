# coding=utf-8
#方法一 读取文件
'''
fo = open('D:\linyouwei\python\demo.txt')
print fo.read()
fo.close()
'''

#方法二 读取文件
'''
fo = file('D:\linyouwei\python\demo.txt')
print fo.read()
fo.close()
'''
'''
#写入文件
f1 = open("D:/linyouwei/python/new.txt",'a')
f1.write('RRRRR')
f1.close()
'''

'''
f1 = open("D:/linyouwei/python/test.txt",'r+')
print f1.read()
f1.write("new")
f1.close()
'''

'''
f1 = open("D:/linyouwei/python/test.txt",'r+')
f1.write("new")
f1.close()
'''

'''
f1 = open("D:/linyouwei/python/line.txt")
print  f1.read()
f1.close()
'''

f1 = open("D:/linyouwei/python/line.txt")
print  f1.readlines()
f1.close()

