#coding=utf-8
class TestDemo:
    __a = 0
    b = 1
    def foo(self):
        self.__a += 1
        self.b += 1
        print self.__a
        print self.b
t = TestDemo()
t.foo()
print t.b
