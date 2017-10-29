#encoding=utf8
def cal(num1,num2,oper='1'):
    if(oper==1):
        return num1 + num2
    elif(oper==2):
        return num1 - num2
    elif(oper==3):
        return num1 * num2
    else:
        return num1 / num2
if __name__ == "__main__":
    while True:
        num1 = input("输入一个数字")
        num2 = input("输入一个数字")
        print("+：1  -：2  *：3  /:4")
        oper = int(input("运算符"))
        if(num1.find('.')== -1 and num2.find('.') == -1):
            result = cal(int(num1), int(num2), oper)
            print(result)
        else:
            result = cal(float(num1), float(num2), oper)
            print(round(result,2))
            print("%.2f"%result)