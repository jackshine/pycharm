# encoding=utf-8
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if(gender=='男'or gender=='女'):
            self.__gender = gender
        else:
            raise ValueError('非男非女')
obj = Student('lin','女')
obj.set_gender('123')
print(obj.get_gender())


