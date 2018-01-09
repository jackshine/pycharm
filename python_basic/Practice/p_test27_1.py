#encoding=utf8
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''
def da(list):
    len = list.__len__()
    len2 = []
    for i in range(len):
        len2.append(list[len-i-1])
    return len2
if __name__ == '__main__':
    list = ['c','d','a','b','g','e']
    print(da(list))