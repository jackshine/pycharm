#encoding=utf8
if __name__ == '__main__':
    a = 0o77
    b = a & 3
    print('a & b = %d' % b)
    b &= 7
    print('a & b = %d' % b)