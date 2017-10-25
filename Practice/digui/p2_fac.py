#encoding=utf8
#1、求1+2+3+……+n的值
def rec(n):
	if n == 1:
		return 1
	s = rec(n-1)*n
	return s
if __name__ == '__main__':
	print(rec(5))
