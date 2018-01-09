#encoding=utf8
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print("%s:%s"%(self.name,self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
if __name__ == "__main__":
    bart1= Student("lin",100)
    print(bart1.get_grade())
    bart1.print_score()
