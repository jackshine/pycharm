def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num = 1
count = 0
while True:
    num += 1
    if isPrime(num):
        count += 1
    if count == 521025:
        break
print(num)