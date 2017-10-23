#encoding=utf8
n=int(raw_input("请输入行数："))
if n%2==0:
    n1=n/2
    n2=n1-1
    for i in range(1,n1+1):
        m=i*2
        print ' '*n2,'*'*m
        n2-=1
    n2=1
    for i in range(n1-1):
        m-=2
        print ' '*n2,'*'*m
        n2+=1
else:
    n1=n//2+1
    n2=n1-1
    for i in range(n1):
        m=i*2+1
        print ' '*n2,'*'*m
        n2-=1
    n2=1
    for i in range(n1-1):
        m-=2
        print ' '*n2,'*'*m
        n2+=1