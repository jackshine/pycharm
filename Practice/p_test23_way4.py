#encoding=utf8

def da(x):
    for i in range(1,x+1):
        a = (x+1)/2+1
        if(i<a):
            to_print_space((x+1)/2-i)
            print((2*i - 1)*"*"),
            print (2*i-1),
            print ""
        elif(i>=a):
            to_print_space(i -(x+1)/2)
            toprint(2*x+1 - i * 2)
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
    da(7)