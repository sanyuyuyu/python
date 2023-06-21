class Timer(object):
    def run(self):
        print('Start...')

class Animal(object):
    def run(self):
        print('Animal is running...')
    def run_twice(self):
        self.run()
        self.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

a = Animal()
b = Dog()
c = Cat()

print(isinstance(a, Animal))
print(isinstance(b, Dog))
print(isinstance(c, Cat))
print(isinstance(a, Dog))

a.run_twice()
b.run_twice()
c.run_twice()