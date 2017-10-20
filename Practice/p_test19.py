#encoding=utf8
def yinzi(x):
    a = []
    for i in range(1,x):
        if (x%i==0):
            a.append(i)
        else:
            continue
    return a
def isWanShu(a,x):
    s = 0
    for i in a:
        s = s+int(i)
    if (s==x):
        return True
    else:
        return False
if __name__ == '__main__':
    c = []
    for i in range(1,10000):
      a  = yinzi(i)
      if(isWanShu(a,i)):
          c.append(i)
    print c