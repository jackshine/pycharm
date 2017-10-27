#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print([['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)] for x in range(1,10)])
a =(' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10))
print(a.__next__())
print(a.__next__())
print(a.__next__())


