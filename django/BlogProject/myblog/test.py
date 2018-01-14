import datetime
print(type(datetime.datetime.now()))
a = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
b = datetime.datetime.strftime(a,'%Y-%m-%d %H:%M:%S')
print(type(b))