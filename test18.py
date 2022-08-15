#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-15 20:55:00
# @Last Modified time: 2022-08-15 21:23:21
dic_char_to_num = {    '1': 1,    '2': 2,    '3': 3,    '4': 4,    '5': 5,    '6': 6,    '7': 7,    '8': 8,    '9': 9,    '0': 0}

def char_to_num(c: str):

    return dic_char_to_num[c] if c in dic_char_to_num.keys() else ''

def str2float(s: str):

    number = reduce(lambda x, y: x * 10 + y, [n for n in map(char_to_num, s) if isinstance(n, int)])

    if '.' in s:

        o = iter(range(len(s)-s.index('.')-1))

        while True:

            try:

                next(o)

                number *= 0.1

            except StopIteration:

                break

    return number



def add(x, y):

    return x + y

def mul(x, y):

    return x * y

def sub(x, y):
    return x - y

sub( mul( add(1,2),  3),  4)


#暂停一秒输出

import time

for i in range(4):

    print(str(int(time.time()))[-2:])

    time.sleep(1)




import math

for i in range(100,200):

    flag=0

    for j in range(2,round(math.sqrt(i))+1):

        if i%j==0:

            flag=1

            break

    if flag:

        continue

    print(i)

print('\nSimplify the code with "else"\n')

for i in range(100,200):

    for j in range(2,round(math.sqrt(i))+1):

        if i%j==0:

            break

    else:

        print(i)


from functools import reduce

def add(x, y):

    return x + y

reduce(add,[1, 3, 5, 3])
 


from functools import reduce

def fn(x, y):

    return x * 10 + y



from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):

    def fn(x, y):

        return x * 10 + y

    def char2num(s):

        return DIGITS[s]
        
    return reduce(fn, map(char2num, s))















































