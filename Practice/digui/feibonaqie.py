#encoding=utf8
#斐波那契额
def f(n):
	if(n==1 or n==2):
		return 1
	s = f(n-1)+f(n-2)
	return s
if __name__ == '__main__':
	for i in range(1,7):
		s = f(i)
		print(s)
