#coding=utf-8
try:
    f = open('abc.txt')
    print 'hello'
except IOError,msg:
    print '你指定的文件不存在'
except NameError,msg:
    print 'error'
finally:
    try:
        f.close()
    except:
        pass
print 'over'