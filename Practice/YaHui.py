#encoding=utf8
'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
'''
#传入一个值就可以得到其
def yang_hui(n):
    a=[[0 for x in range(n)] for y in range(n)]
    #i是行
    for i in range(n):
        #j是列
        for j in range(n):
            if (j==0 or i==j):
                a[i][j] = 1
            if(i!=j and j!=0):
                a[i][j] = a[i-1][j-1]+a[i-1][j]
            if(i>=j):
                print(a[i][j]),
        print("")
    return a
if __name__ == '__main__':
    yang_hui(7)
