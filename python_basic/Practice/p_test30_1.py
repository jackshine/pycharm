#encoding=utf8
'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
解决方法：逆序得到的原来的数进行对比
'''
#得到每个位数的长度
def is_huiwen(x):
	if(getParam(getNum(x))==x):return '是回文数'
	else: return '不是回文数'
#传入列表，返回他的整数值
def getParam(list):
	len = list.__len__()
	s = 0
	for i in range(len):
		for j in range(len-i-1):
			list[i]=list[i]*10	
		print(list[i])
		s = s + list[i]
	return s	
#传入整数，得到其逆序的列表	
def getNum(x):
	s = []
	while True:
		a = int(x % 10)
		if(a ==0):
			break
		else:
			s.append(a)
			x = int(x / 10)
	return	s
if __name__ == '__main__':
    print (is_huiwen(123454321))