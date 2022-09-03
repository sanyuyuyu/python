#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-02 14:15:39
# @Last Modified time: 2022-09-03 20:57:30
class people:
    def __init__(self):
        pass 

    def set_name(self, name):
        self.__name = name 

    def get_name(self):
        return self.__name 

    def greet(self):
        print("What is your old are you ? I am {}.".format(self.name))


p = people()
p.set_name('18')
print(p.get_name())



class people:
    def __init__(self):
        pass 

    def set_name(self, name):
        self.__name = name 

    def get_name(self):
        return self.__name 

    def greet(self):
        print("What is your old are you ? I am {}.".format(self.name))


class boy(people):

    def run(self):
        print("i can run .")

    def greet(self):
        print("i love fish .")

b = boy()
b.name = 'bob'
b.greet()



class girl(people):

    def say(self):
        print("i am beautiful .")

    def greet(self):
        print("i am ok .")



class People:
    def __init__(self, role, name, age):
        self.name = name
        self.age = age
        self.role = role
 
    def infos(self):
        return [
            f"name:{self.name}",
            f"age:{self.age}",
            f"role:{self.role}"
        ]
 
class Student(People):
    def __init__(self, no, name, age):
        super().__init__("student", name, age)
        self.no = no


def infos(self):
        info_list = super().infos()
        info_list.append(f'no:{self.no}')
        return info_list
 
 
class Teacher(People):
    def __init__(self, access_key, name, age):
        super().__init__("teacher", name, age)
        self.access_key = access_key
 
    def infos(self):
        info_list = super().infos()
        info_list.append(f'access_key:{self.access_key}')
        return info_list
       
 
 
if __name__ == '__main__':
    peoples = [
        Teacher("ajladfjkadf", "Linus", 0)
    ]
 
    for i in range(0, 3):
        s = Student(i, f'somebody_{i}', 20+i)
        peoples.append(s)
 
    for p in peoples:
        print()
        for info in p.infos():
            print(info)






from random import choice

class ddivergence:

    def __init__(self,name='robot'):
        self.name = name 
        pass 

    def getChoice(self,name=None):
        if name is not None:
            self.name = name 
        self.__lists = ['yes','no']
        result = choice(self.__lists)
        print(self.name,':yeah',resultb)



class Point:
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y 
        self.z = z 


import abc
class shuiguo(metaclass=abc.ABCMeta):
    
    all_type='sg'

    def name(self):
        pass

    def func(self):
        pass


class Apple(shuiguo): #子类继承抽象类，必须定义read和write方法
    def name(self):
        print('我是苹果')

    def func(self):
        print('好吃')


    def func(self):
        print('yunfeizhike')


apple =Apple()


apple.func()


print(apple.all_type)


import abc 
class BasePoint:
    def __init__(self, x, y, z) -> None:
        self.x = x 
        self.y = y 
        self.z = z 
    @abc.abstractmethod
    def dot(self, right):
        pass
class Point(BasePoint):
    def __init__(self, x, y, z) -> None:
        super().__init__(x, y, z)

    def dot(self, right):
        return self.x*right.x+self.y*right.y+self.z*self.z

if __name__ == '__main__':
    p1 = Point(0, 1, 2)
    p2 = Point(2, 4, 6)
    p1 = BasePoint(0, 1, 2)
    p2 = BasePoint(2, 4, 6)
    assert p1.dot(p2) is None



class Apple():
    def name(self,name):
        self.__name = name 

    def getName(self):
        return self.__name

class Apple():
    def __setAge(self,age):
        self.__age = age 

    def getName(self):
        return self.__name 

    def info(self,age):
        self.__setAge(age);
   

def getAge(self):
    return self.__age



def info(self,age):
    if age < 1:
       raise ValueError('too small')
    elif age > 100:
       raise ValueError('too big')
    else:
      self.__age = age










































































