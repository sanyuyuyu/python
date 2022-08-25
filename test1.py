#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date:   2022-07-23 22:08:30
# @Last Modified time: 2022-08-25 21:50:12

print('hello world')
print('200+300=',200+300)
a = 200 + 300 
print()



# name = input('Please enter your name:')
# print('hello,', name)
a = 100 
if 1>a >= 0:
    print("a1", a)
elif 2>a >=1:
    print("a2",a)
elif a >=3:
    print("a3",a)
else:
    print(-a)


def sum1(n: int):
    return (n+1)*n // 2


def test1():
    ...


sum2 = sum1(10000)
print(sum2)


def sum_of_a_and_b(a: int,b: int):
    return a + b


a1 = 3
a2=4

print(sum_of_a_and_b(a1,a2))



def text1(a1: str,a2: str):
    return a1 + a2


print(text1("abc", "cba"))



def text2(a: int,b: int):
    return a ** b 


def text3(a1:int,a2:int,a3:int):
    return (a1 + a2)* a3


def get_d(a, b):
    return 100 * (a + b)


def test_git():
    ...


def test4():
    ...





age = 16
if age >= 18:
    print('adult')
else:
    print('teenager')


print('i\'m ok')
print("i'm ok")

a = 'abd'
b = a
a = 'xye'
print(b)

ord('A')


def beauty(y: int,z: int):
    return y*z


b'ABC'.decode('ascii')


len('beauty')


"chinese".encode('utf-8')




print('%.f2' % 3.1415926)





'growth rate: %d %%' % 7


zoo = ['monkey', 'dog', 'snake']


temp = input ('please guess a number')
guess = int(temp)


if guess == 8:
    print('you are good')
    print('perfect')
else:
    print('it is 8')
print('end')


print("let's go!go!go!")


print('chinese.\nausia')



print("D:\\three\\abandan\\now")


a = {"old":"older","young":"younger","slow":"slower"}
b = dict(old="older",young="younger",slow="slower")
c = dict([("old","older"),,("young","younger"),("slow","slower")])
d = dict({"old":"older","young":"younger","slow":"slower"})
e = dict({"old":"older","young":"younger"},slow="slower")
f = dict(zip(["old","young","slow"],["older","younger","slower"]))
a == b == c == d == e ==f


d = dict.fromkeys("fish",250)
d
{'f':250,'i':250,'s':250,'h':250 }
d['f'] = 70
{'f':70,'i':250,'s':250,'h':250 }
d.clear()
{}

d = dict.fromkeys('fish')
{'f':none,'i':none,'s':none,'h':none }


d.setdefault('C',"code")
'67'
d.setdefauly('c',"code")
'code'
keys = d.keys()
values = d.values()
items = d.items()
e = d.copy


d = {'F':70,'i':105,'s':115,'h':104,'C':67}
b = {v:k for k,v in d.items()}
b
{70:'f',105:'i',115:'s',104:'h',67:'c'}
c = {v:k for k,v in d.items() if v > 100}
d = {x:ord(x) for x in "fishc"}
{'F':70,'i':105,'s':115,'h':104,'C':'67'}
d = {x:y for x in [1,3,5] for y in [2,4,6]}
{1:6,3:6,5:6}



 {'fish','tiger'}
{s for s in 、'fish'}
{'s','h','i','f'}
set ('fish')
{'s','h','i','f'}
for each in s:
    print(each)
set ([1,1,3,4,5])
{1,3,4,5 }
s.union({1,2,3})
s.intersection({1,2,3})
s.difference({1,2,3})
s.symmetric_difference("python")
 







t = frozenset('fish')
s = set('fish')
s.update([1,1],'23')
s.intersection_update('fish')
s.remove('fish')
s.discard('fish')
s.pop('fish')


hash(1)
1
hash(1.0)
1
hash(1.001)

x = {1,2,3}
y = {4,5}
x = frozenset(x)
y = {x, 4, 5}
y
{frozenset({1,2,3})4,5}


def myfunc():
    pass
myfunc()

def myfunc():
    for in range(3):
        print('i love python')
 
 def myfunc(name):
    for i in range(3):
        print(f'i love {name}')

myfunc("name" )
myfunc("name",5)


def div(x,y):
    z = x / y
    return z
div(4,2)
2.0

def div(x,y):
    return x / y

def div(x,y):
    if y == 0:
        return("除数不能为零")
    else:
        return x / y

def div(x,y):
    if y == 0:
        return("除数不能为零")
    return x / y  


def myfunc():
    pass
print(myfunc())
none

def myfunc(s,vt,o):
    return"".join((o,vt,s))
myfunc("dog","tiger","snake")
'snake tiger dog'
myfunc(o="dog",vt="tiger",s="snake")

def myfunc(s,vt,o="dog"):
    return"".join((s,vt,o))
 

def abs(a,/,b,c):
    print(a,b,c)


def myfunc(*args):
    print(“有{}个参数。”。formate(len(args)))
    print("第二个参数是：{}".formate(args([1]))
def myfunc(*args):
    print(type(args))
myfunc(1,2,3,a=4,b=5)
def myfunc(**kwargs):
    print("kwargs")
myfunc(a=1,b=2,c=3)
{'a':1,'b':2,'c':3}

def myfunc(a,*b,**c):
    print(a,b,c)
myfunc(1,2,3,4,x=5,y=6)
1 (2, 3, 4){'x':5,'y':6}
help(str.format)


args = (1, 2, 3, 4)
def myfunc(a, b, c, d):
    print(a,b,c,d)

def myfunc():
    x = 520
    priint(x)
x = 250
def myfunc():
    print(x)
myfunc()
520
print(x)
250
x = 250
def myfunc():
    global x
    x = 520
    print(x)
 myfunc()
 520
 print(x)
 520    


def funA():
    x = 520
    def funB():
        x = 880
        print("in funB, x =",x)
    print("in funA, x =",x)

def funA():
    x = 520
    def funB():
        x = 880
        print("in funB, x =",x)
    funB()
    print("in funA, x =",x)
funA()
in funB,x = 880
in funA,x = 520
  

def funA():
    x =520
    def funB():
        nonlocal x
        x = 880
        print("in funB, x =",x)
    funB()
    print("in funA, x =",x)
funA()
in funB,x = 880
in funA,x = 880

def funA():
    x = 880
    def funB():
        print(x)
    funB()
funny = funA()
funny
def power(exp):
    def exp_of(base):
        return base ** esp
    return esp_of
square = power(2)
cube = power(3)
 

def outer():
    x = 0
    y = 0
    def inner(x1,y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"现在，x = {x1},y = {y1}")
    return inner


import time
def time_master(func):
    print("开始运行")
    start = time.time()
    func()
    stop = time.time()
    print(“结束运行”)
    print(f"一共消耗了{(stop-start):.2f}秒。 ")



def myfunc():
    time.sleep(2)
    print("hello")
 time_master(myfunc )   
myfunc = time_master(myfunc)

@time_master  
def myfunc():
    time.sleep(2)
    print("hello")
myfunc



def add(func):
    def inner():
        x = func()
        return x + 1
    return inner

def cube(func):
    def inner():
        x = func()
        return x * x * x
    return inner

def suqare(func):
    def inner():
        x = func()
        return x * x
    return inner

@add
@cube
@square
def test():
    return 2
print(test())


import time
def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"[{msg}]一共耗费了 {(stop-start):.2f}")
        return call_func
    return time.master

def funA():
    time.sleep(1)
    print("funA")

def funB():
    time.sleep(1)
    print("funB")

funA = logger(msg="A")(funA)
funB = logger(msg="B")(funB)



def squareX(3):
    return x * x

squareY = lambda y : y * y

y = [lambda x : x * x, 2, 3]
y[0](y[1])
0
y[0](y[2])

mapped = map(lambda x : ord(x) + 10, 'fish')
list(mapped)


def boring(x):
    return ord(x) + 10
list(map(boring,'fish'))
[80,115,125,114,77]
list(filter(lambda x : x % 2, range(10)))
[1,3,5,7,9]


def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1

for i in counter():
    print(i) 
c = counter()

def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1 + back2
f = fib()

(i ** 2 for i in range(10))
for i in t:
    print(i)

def fun(i):
    if i > 0:
        print('AWCSU')
        i -= 1
        func(i)

def factiter(n):
    result = n
    for i in range(1,n):
        result *=1
    return result

def factrecur(n):
    if n == 1:
        return 1
    else:
        return n * factrecur(n-1)

def fibiter(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a = b 
        b = c
        n -= 1
    return c 

def fibrecur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibrecur(n-1) + fibrecur(n-2)





def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z) # 如果只有一层，直接将金片从x移动到z层
    else:
        hanoi(n-1, x, z, y) # 将x上n-1个金片移动到y
        print(x, '-->', z)  # 将最低下的金片从x移动到z
        hanoi(n-1, y, x, z) # 将y上的n-1个金片移动到z 
n = int(input('请输入汉诺塔的层数：')）
hanoi(n,'A','B','C')



def times(s:str, n:int) -> str:
    return s * n
times('fish',3)

def times(s:str = "fish", n:int = 3) -> str:
    return s * n

def times(s:list, n:int = 3) -> str:
    return s * n

def times(s:list[int],n:int = 3) -> list:
    return s * n

def times(s:dict[str, int], n:int = 3) -> list:
    return list(s.keys()) * n

times._name_
times._annotation_


def add(x, y):
    return x + y
import functools
functools.reduce(add, [1,2,3,4,5])

add(add(add(add(1, 2), 3), 4), 5)
functools.reduce(lambda x,y:x*y, range(1:11))
square = functools.partial(pow, exp=2）
cube = functools.partial(pow, exp=3)


import time
import functools

def time_master(func):
    @functools.wraps(func)
    def call_func():
        print("开始运行程序...")
        start = time.time()
        func()
        stop = time.time()
        print("结程序运行...")
        print(f"一共消耗了 {(stop -start):.2f}秒。")
    return call_func
def myfunc():
    time.sleep(2)
    print("i love eat fish.")



f = open("fish.text","w")
f.write('I love python.')
f.writelines(["I love fish.\n","I love cat."])
f.close()
f = open("fishc.text","r+")
f.readable()
f.writable()
for each in f:
    print(each)
f.read()
f.tell()
f.seek(0)
f.readline()
f.flush()
f.truncate()





from pathlib import path
path.cwd()
q = p / "Fishc.txt"

p.is_dir()
true
q.is_dir()
False 

p.is_file()
q.is_file() 

p.exists()
q.exists()
path("C:/404").exists()
p.name

q.name
"Fishc.txt"

q.stem
'Fishc'
q.suffix
'.txt'
p.stat().st_size
path("./dox")

p.iterdir()
for each in p.iterdir():
    print(each)

[x for x in p.iterdir() if x.is_file()]


f = open("FishC.txt","w")
f.write("I love fish.")
f.close()

with open("FishC.txt","w") as f:
    f.write("I love fish.")


import pickle
x, y, z = 1, 2, 3
s = 'fishc'
l = ["tiger", 520, 3.114]
d = {"one":1, "two":2}
with open("data.pkl","wb")as f:
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(z, f)
    pickle.dump(s, f)
    pickle.dump(l, f)
    pickle.dump(d, f )


import pickle
with open("data.pkl", "rb")as f:
    x = pickle.load(f)
    y = pickle.load(f)
    z = pickle.load(f)
    s = pickle.load(f)
    l = pickle.load(f)
    d = pickle.load(f)
print(x, y, z, s, l, d, sep"\n")


import pickle
with open("data.pkl","rb")as f:
    x, y, z, s, l, d = pickle.load(f)
print(x, y, z, s, l, d, sep"\n" )



def exchange(dollar, rate=6.32):
    

try:
    1 / 0
    520 + "fishc"
except ZeroDivisionError:
    print("除数不能为零")
except ValueError:
    print("值不正确"）
except TypeError:
    print("类型不正确。")
 
















t2.sleep()
class C:
    def hello():
        print("你好")

class C:
    def get_self(self):
        print(self)

c = C()
c.get_self()

class A:
    x = 520
    def hello(self):
        print("你好")
class B(A):
    pass

b = B()
b.x
520

class B(A):
    x = 880 
    def hello（self):
    print(“你好”) 

b = B()
b.x
b.hello()
你好  

isinstance(b, B)
isinstance(b, A)
issubclass(A, B)
issubclass(B, A)

class B:
    x = 880
    y = 250
    def hello(self):
        print("你好 ")

class C(A,B):
    pass

c = C()
c.x

class Turtle:
    def say(self):
        print("不积硅步，无以至千里")

class Cat:
    def say(self):
        print("喵")

class Dog:
    def say(self):
        print("wolf wolf")

class Garden:
    t = Turtle()
    c = Cat()
    d = Dog()
    def say(self):
        self.t.say()
        self.c.say()
        self.d.say()
g = Garden()
g.say()
不积硅步，无以至千里
喵
wolf wolf


class C:
    def get_self(self):
        print(self)

c = C()
c.get_self()
d = C()
d.x = 250


c.__dict__
{'x':520}

d.__dict__
{'x':250}
d.y = 660
d.__dict__
{'x': 250, 'y': 660}
class C:
    def set_x(self,v):
        self.x = v


c = C()
c.__dict__
{}
c.set_x(250)
c.__dict__
{'x':250}
c.x
250


class C:
    x = 100
    def set_x(self,v):
        x = v

c = C()
c.set_x(250)
c.x
100
C.x
100
C.x = 250
c.x
c.__dict__
{}

class C:
    pass

C.x = 250
C.y = "fish"
C.z = [1, 2, 3]
print(C.x)
250

d = {}
d['x'] = 250
d['y'] = "fish"
d['z'] = [1, 2, 3]


c = C()
c.x = 250
c.y = "fish"
c.z = [1, 2, 3]


class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x *self.y

c = C(2, 3)
c.add()


class D():
    def __init__(self,x, y, z):
        C.__init__(self, x, y)
        self.z = z
    def add(self):
        return C.add(self) + self.z
    def mul(self):
        return C.mul(self) * self.z

d.add()
d.mul()


class A:
    def __init__(self):
        print("A")

class B1(A):
    def __init__(self):
        A.__init__(self)
        print("B1")

class B2(A):
    def __init__(self):
        A.__init__(self)
        print("B2")

class C(B1, B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print("c")
   

class B1(A):
    def __init__(self):
        super().__init__()
        print("B1")

class B2(A):
    def __init__(self):
        super().__init__()
        print("B2")

class C(B1, B2):
    def __init__(self):
       super().__init__()
        print("c")























class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f"我叫{self.name}, 今年{self.age}岁。")

class FlyMixin:
    def fly(self):
        print("fly fly")

class Pig(Animal):
    def special(self):
        print("pig pig")
p = Pig("ss",5)
p.say()
p.special()


class Displayer:
    def display(self, message):
        print(message)

class LoggerMixin:
    def log(self, message, filename="logfile.txt"):
        with open(filenmae, "a") as f:
            f.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)

class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename="subclasslog.txt")

subclass = MySubClass()
subclass.display("This is a test.")


len(["fish", "dog"])
len({"name":"dog", "age":18})

class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__("正方形")
        self.length = length
    def area(self):
        return self.length * self.length

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("三角形")
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height / 2


class B1(A):
    def __init__(self):
        A.__init__(self)
        print("B1")

class B2(A):
    def __init__(self):
        A.__init__(self)
        print("B2")

class C(B1, B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print("c")
   
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"{self.name},{self.age}")
    def say(self):
        print("miao")


   
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"{self.name},{self.age}")
    def say(self):
        print("wolf")


def animal(x):
    x.intro()
    x.say()


class Bicycle:
    def intro(self):
        print("")
    def say(self):
        print("")


class C:
    def __init__(self, x):
        self.__x = x
    def set_x(self, x):
        self.__x = x
    def get_x(self):
        print(self.__x)
c = C(250)
c.__x
c.get_x(520)
c.get_x()
c.__dict__ 
{'_C__x': 520}

class D:
    def __func(self):
        print("Hello ")
d.__func()

class C:
    def __init__(self, x):
        self.x = x
c = C(250)
c.x
250
c.__dict__
{'x':250}

class C:
    __slots__ = ["x", "y"]
    def __init__(self, x):
        self.x = x
c = C(250)
c.x
250
c.y = 520


class D:
    __slots__ = ["x", "y"]
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class E:
    pass
e = E(250)
e.x
e.__slots__


class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return super().__new__(cls, string)

cs = Capstr("fish")
cs
'FISH'
cs.lower()
'fish'
cs.capitalize()
'Fish'

class C:
    def __init__(self):
        print("i am coming")
    def __del__(self):
        print("i am back number")


class D:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        globa x
        x = self
class E:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def __del__(self):
        self.func(self)


def outter():
    x = 0
    def inner(y=None):
        nonlocal x
        if y:
            x = y
        else:
            return x
    return inner

f.outter()



class S(str):
    def __add__(self, other):
        return len(self) + len(other)





























































































































































