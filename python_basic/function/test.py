def getsum(a,b,*num):
    print(a,b,num)
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum


nums = (1, 2, 3)
getsum(*nums)
