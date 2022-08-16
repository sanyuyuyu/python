#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-16 17:42:29
# @Last Modified time: 2022-08-16 19:48:20
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,

          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):

    for i in range(len(s)):

        if s[i] =='.':

            a = s[:i]

            b = s[i+1:]

    def char2num(s):

        return DIGITS[s]

    def f1(x,y):

        return x*10 + y

    c = reduce(f1,map(char2num,a))

    d = reduce(f1,map(char2num,b))

    return c + d*10**(-len(b))



def str2float(s):

    l = len(s)

    i = s.index('.')

    def str2int(x):

        return int(x)

    def intXint(x,y):

        return int(x)*10 + int(y)

    s1 = reduce(intXint, list(map(str2int, s[:i])))

    s2 = reduce(intXint, list(map(str2int, s[i+1:])))

    return s1+s2*(0.1**(l-i-1))


height = 1.75
weight = 80.5

bmi = weight/(height*2)

if bmi <18.5:

    print('BMI为%d,体重过轻' % bmi)

elif bmi >= 18.5 and bmi < 25:

    print('BMI为{0:.1f},体重正常'.format(bmi))

elif bmi >= 25 and bmi < 28: 

    print('BMI为%s,体重过重'.format(bmi))

elif bmi >= 28 and bmi < 32: 

    print(f'BMI为{bmi:.1f},体重肥胖')

elif bmi >= 32 :    

     print(f'BMI为 {bmi:.1f} ,体重严重肥胖')



def calc_sum(*args):
    
    ax = 0

    for n in args:

        ax = ax + n 

    return ax



def lazy_sum(*args):

    def sum():

        ax = 0

        for n in args:

            ax = ax + n

        return ax

    return sum


def count():

    fs = []

    for i in range(1, 4):

        def f():

             return i*i

        fs.append(f)

    return fs

f1, f2, f3 = count()



def count():

    def f(j):

        def g():

            return j*j

        return g

    fs = []

    for i in range(1, 4):

        fs.append(f(i)) 
         ?
                                                                                 
    return fs




































