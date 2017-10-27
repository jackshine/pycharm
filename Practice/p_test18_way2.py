#encoding=utf8
"题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。"
def qiuhe(a,x):
    sum = 0
    for j in range(1,x+1):
        s =0
        for i in range(j):
            s += 10**i
        sum += s
    return sum*a
if __name__ =="__main__":
    s =qiuhe(2,3)
    print(s)
