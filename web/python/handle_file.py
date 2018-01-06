file = open('data.txt',encoding='utf-8')
for line in file:
    line=line.strip('\n')
    result = line.split('*')
    print(result[1])