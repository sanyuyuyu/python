#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date:   2022-07-23 22:08:30
# @Last Modified time: 2022-08-01 22:28:17

print('hello world')
print('200+300=',200+300)

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


















