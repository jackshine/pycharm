#encoding=utf-8
s = '中文'
print(type(s))
b = bytes(s,encoding='utf-8')
print(b)
a = b'\xe4\xb8\xad\xe6\x96\x87' #bytes类型
s1 = str(a,encoding='utf-8')
print(s1)