#encoding=utf8
#九九乘法表
for x in range(1,10):
	for y in range(x,10):
		print('{}*{}={}'.format(x,y,x*y),end='')
	print('')