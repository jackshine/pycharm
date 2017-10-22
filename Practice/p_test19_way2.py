#encoding=utf8

from sys import stdout

for j in range(2, 1001):
    k = []
    n = 0
    s = j
    for i in range(1, j):
        if j % i == 0:
            n += 1   #n是计算有多少个因子
            s -= i
            k.append(i)
    if s == 0:
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print("")