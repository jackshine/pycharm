#encoding=utf8
def jiecheng(n):
	s = 1
	for i in range(1,n+1):
		s = s*i
	print(s)
	return s
def jc_sum(n):
	s = 0
	for i in range(1,n+1):
		s = s + jiecheng(i)
	print(s)
if __name__ == '__main__':
   jc_sum(3)
