class Animal(object):
    def run(self):
        print('animal can run...')

class Dog(Animal):
    def run(self):
        print('Dog can run....')
    def eat(self):
        print('Dog can eat...')

class Cat(Animal):
    def cry(self):
        print('miao....')


def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise():
    def run(self):
        print('Tortoise is running slowly...')

