#encoding=utf8
#斐波那契
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return '333'
if __name__ == '__main__':
    for g in fib(6):
        print(g)