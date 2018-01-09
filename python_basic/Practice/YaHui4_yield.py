#encoding=utf8
def triangles(max):
    L = [1]
    n = 0
    while n<max:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]
        n +=1
if __name__ == '__main__':
    for i in triangles(10) :
        print(i)