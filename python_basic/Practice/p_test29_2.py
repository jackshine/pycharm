#encoding=utf8
'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
#得到每个位数的长度
def getNum(x):
    while True:
        b = x%10
        print(b)
        if(int(x/10)==0):
            break
        else:
            x = int(x/10)
if __name__ == '__main__':
    print (getNum(324))