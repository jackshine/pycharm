class A:
    def sum(self, n):
        return 0


class B(A):
    def __init__(self):
        self.arr = [A(), self]

    def sum(self, n):
        return self.arr[n != 0].sum(n - 1) + n

b = B()
print(B().sum(3))
