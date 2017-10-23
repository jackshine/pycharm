#encoding=utf8

def qiuhe(c,x):
    s = []
    for i in range(x):
        a = 10**i
        s.append(a)
    b = 0
    for j in s:
        b += j
    return c*b
if __name__ =="__main__":
    sum = 0
    #多少个数:
    accout = 5
    #个位数是:
    num = 2
    for i in range(1,accout+1):
        sum += qiuhe(num,i)
    print sum
