# encoding=utf-8
class Student(object):
    name = ''
    score = ''
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_s(self):
        print(self.name)
        print(self.score)
if __name__ == "__main__":
    pass