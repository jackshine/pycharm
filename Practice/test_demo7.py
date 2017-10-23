#encoding=utf8
#将一个列表的数据复制到另一个列表中。
#方法1
list = ["11","dd","cc"]
'''
a = list[:]
print(a)
'''
#方法2
'''
b = []
for s in range(len(list)):
    b.append(list[s])
print b

'''
#方法3
'''
b = [i for i in list]
print b
'''

#浅拷贝应用



