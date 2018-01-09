#encoding=utf8
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def set_score(self,score):
        self.__score = score
    def set_score(self,__score):
        if 0 <= __score <= 100:
            self.__score = __score
        else:
            raise ValueError('bad score')
if __name__ == "__main__":
    bart1= Student("lin",100)
    print(bart1.get_name())
