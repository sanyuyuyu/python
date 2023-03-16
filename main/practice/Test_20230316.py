file = open('text.txt')

file.readline()

file.readlines()

type(file.readlines()) #获取读取数据的类型

file = open('text.txt','w+') #以读写方式打开文本文件

file.write('hello .\n')  

'''
import pygame

def main():

	pygame.init()

	pygame.quit()

if __name__ == '__main__':

	main()
'''
class Person:
 
    def __init__(self,name,age):
 
        self.name=name
 
        self.age=age
 
    def setName(self,name):
 
        self.name=name
 
    def setAge(self,age):
 
        self.age=age
 
    def show(self):
 
        print(self.name,self.age)
 
class Student(Person):
 
    def __init__(self,name,age,major):
 
        Person .__init__(self,name,age)
 
        self.major=major
 
    def setMajor(self,major):
 
        self.major=major
 
    def show(self):
 
        print(self.name,self.age,self.major)
 
p=Person('陈一',21)
 
p.setName('程二')
 
p.setAge(20)
 
p.show()
 
f=Student('陈二',15,'初中生')
 
f.setName('陈一')
 
f.setAge(21)
 
f.setMajor('大数据')
 
f.show()