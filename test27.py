#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-01 18:50:40
# @Last Modified time: 2022-09-01 19:33:34
class Person(): #Person:类的名称
    def  __init__(self):  #对象本身
        pass 

    def set_name(self, name):
        self.name = name

    def set_name(self):
        return self.name

    def greet(self):
        print("What is weather today ? {}.").format(self.name)

class Student:
    def __init__(self, no, name, age):
       self.no = no 
       self.name = name
       self.age = age 

    def dum(self):
        infos = [f"*no:{self.no}",
                 f"*name:{self.name}",
                 f"*age:{self.age}"]
        for info in infos:
            print(info)


class Person():
    type = 'ren' #静态字段
    def __init__(self):
            #普通字段
        self.name = 'mingzi'
        pass

    def set_name(self, name):
        self.name = name

p = Person()
p.type = 'woman'
p.name = 'man'
print(Person.type)
print(p.name)

class Human:
    count = 0
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    

    def setName(name):
        self.name = name 


    def add_count(cls):
        cls.count += 1
     

    def get(cls):
        return cls.count
     

class Student:
    def __init__(self, no, name, age):
        self.no = no 
        self.name = name 
        self.age = age 

def test():
    students = []
    for i in range(0, 3):
        s = Student(i, f'somebody_{i}', 20+i)
        students.append(s)

    for s in students:
        print('')
        print(f"* no:{s.no}")
        print(f"* name:{s.name}")
        print(f"* age:{s.age}")
if __name__ == '__main__':
    test()



























