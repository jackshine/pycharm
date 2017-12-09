# encoding = utf-8
class Animal(object):
    def run(self):
        print('Animal is running..')

class Dog(Animal):
    def run(self):
        print('dog is running..')
    def eat(self):
        print('Eating meating..')
class Cat(Animal):
    pass

dog = Dog()
dog.run()
print(isinstance(dog,Animal))