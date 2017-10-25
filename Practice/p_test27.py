#encoding=utf8
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''
def rev(list,i):
    if i == list.__len__() :
        return 
    a = rev(list, i+1)
    print(list[i])
    return list[i]

if __name__ == '__main__':
    list = ['c','d','a','b','g','e']
    rev(list, 0)
