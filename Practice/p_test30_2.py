#encoding=utf8
'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
解决方法：逆序得到的原来的数进行对比
'''
#得到每个位数的长度
def is_huiwen(x):
    if(str(x)[-1::-1]==str(x)):return "是回文数"
    else:return "不是回文数"
if __name__ == '__main__':
    print (is_huiwen(3342342))