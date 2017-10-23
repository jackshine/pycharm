#encoding=utf8

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
    print s
