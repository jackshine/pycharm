#encoding=utf8
import math
def yuan():
    pass\
#求y轴坐标
def y_axis(r):
    #r为半径
    for i in range(r,-6,-1):
        x1 = math.sqrt(r*r+i*i)+r
        x2 = -math.sqrt(r*r+i*i)+r
        print (x1,x2)
def print_star(x):
    for i in x:
        print ""
if __name__ == "__main__":
    y_axis(5)