#encoding=utf8
def jiecheng(n):
	if(n == 1): 
		return 1
	s = jiecheng(n-1)*n
	return s 

if __name__ == '__main__':
   s = jiecheng(4)
   print s
