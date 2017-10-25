#encoding=utf8
'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
def digits(n):
    s = str(n).__len__()
    return s
def Rev(m):
    pass
#得到每个位数的值
def getNum(x):
     a = x/1%10
     b = x/10%10
     c = x/100%10
     return a,b,c
if __name__ == '__main__':
    x = int(input("输入一个数："))
    print (digits(x))
    print (getNum(x))