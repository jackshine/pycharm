#encoding=utf8
# #输出 9*9 乘法口诀表。
for i in range(1,10):
    for j in range(1,10):
        s = i*j
        if(j>i):
            break
        print "%s*%s="%(i,j)+str(s),
    print ''
