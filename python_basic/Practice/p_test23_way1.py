
#encoding=utf8
#打印一下图
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
def da():
    for i in range(1,8):
        if(i<5):
            to_print_space(4-i)
            toprint(2*i-1)
            print ""
        elif(i>=5):
            to_print_space(i -4)
            toprint(15 - i * 2)
            print ""
#打印X个星号
def toprint(x):
    for i in range(x):
        print "*",
#打印X个空格
def to_print_space(x):
    for i in range(x):
        print " ",
if __name__ == '__main__':
    da()