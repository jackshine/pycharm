#encoding=utf8
#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
a = []
def YinZi(x):
    print(type(x))
    for j in range(int(x)):
        print(x%j)
        if(x%j==0):
            a.append(x)
        else:
            continue
if __name__ == '__main__':
    #求50的所有因子
    YinZi(50)