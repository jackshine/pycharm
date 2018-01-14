import datetime

d1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
d4 = datetime.datetime.strptime(d1,'%Y-%m-%d %H:%M:%S')
print(type(d4))