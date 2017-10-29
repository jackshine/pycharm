#encoding=utf8
from functools import reduce
def char2num(s):
    a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return a
l = list(map(char2num,'13579'))
print(list(l))