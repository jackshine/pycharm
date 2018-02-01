def isshu(s):
    for i in range(2, s):
        if s % i == 0:
            return False
        if i == int(s / 2):
            return True


s = 1
i = 3
while True:
    if isshu(i) == True:
        s = s + 1
    if s == 251025:
        print(i)
        break
    i += 1