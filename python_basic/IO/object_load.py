import json
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
json_str = '{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str,object_hook=dict2student))