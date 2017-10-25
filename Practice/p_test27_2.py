#encoding=utf8
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''
def da(list):
    len = list.__len__()
    for i in range(int(len/2)):
        a = 0
        a = list[i]
        list[i] = list[len-1-i]
        list[len-1-i] = a
    return list
if __name__ == '__main__':
    list = ['c','d','a','b','g','e']
    print(da(list))