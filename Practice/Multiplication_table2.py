#encoding=utf8
#九九乘法表
def multi_table(n):
	L = [str(i) + "*" + str(j) +"="+str(i*j) for i in range(1,10) for j in range(i,10) ]
	return L
if __name__ =="__main__":
    print(multi_table(9))