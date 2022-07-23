#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date:   2022-07-23 22:08:30
# @Last Modified time: 2022-07-23 22:10:33

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
    return 100 * (a +b)



















































