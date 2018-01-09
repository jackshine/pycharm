#encoding=utf8
'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
#得到每个位数的长度
def getLen(x):
    n = 1
    while True:
        if(int(x/10)==0):
            break
        else:
            x =int(x/10)
            n +=1
    return n
def getNum(x):
    a = []
    for i in range(getLen(x)):
        b = x%10
        a.append(b)
        if(int(x/10)!=0):
            x = int(x/10)
        else:
            break
    return a
if __name__ == '__main__':
    print (getNum(56546456456))