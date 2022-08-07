#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-07 17:57:35
# @Last Modified time: 2022-08-07 19:01:40
a = 200 + 300
print('200 + 300=',' ',a)
print('200 + 300=', a, a, a)
print("{0}".format(a))
print(f"a:{a},b:300,c")
b = 3
c = 4
d = 5
print("{0}{1}{2}{3}".format(a,b,c,d))
print(f"{a}{b}{c}{d}")
print(f"i am beautiful")

a = 200
input(a)


if __name__=="__main__":
    a = input()
    print(type(a))
    b = input()
    print(type(b))
    c = a + b
    print(c)
    print(type(c))





























