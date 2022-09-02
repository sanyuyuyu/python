#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-02 14:15:39
# @Last Modified time: 2022-09-02 21:13:08
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




































































