#encoding=utf8
#斐波那契
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

if __name__ == '__main__':
	fib(6)
