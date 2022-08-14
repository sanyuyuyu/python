#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-14 17:30:35
# @Last Modified time: 2022-08-14 20:07:33
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2


def trim(s):
    if s !='':
        while s[0] == ' ' and len(s) > 1:
            s = s[1:]
        while s[-1:] == ' ' and lens(s) > 1:
            s = s[:-1]
        if s == ' ':
            s = ''
    return


def trims(s):
    l = list(s)
    x = 0
    y = -1
    while x < len(s):
        if l[x]=='':
            x = x+1
        else:
            break
    while y <=0:
        if l[y]=='':
            y = y-1
        else:
            break
    print(s[x:y+1])
trim('ROger federer')

  

def findMinAndMax(L):

    if L == []:

        return (None,None)

    min = max = L[0]

    for i in L:

        if i < min:

            min = i

        if i > max:
            max = i
        return (min,max)



def fib(max):

    n, a, b = 0, 0, 1

    while n < max:

        print(b)

        a, b = b, a + b

        n = n + 1

    return 'done'



def pascalsTringle():

    l = [1]

    while True:

        yield l

        length = len(1)

        l1 = [l[i - 1] + 1[i] if i > 0 and i < length else l for i in range(0, length + 1)]

        l = list(11)





def fib(max):

    n, a, b = 0, 0, 1

    while n < max:

        a, b = b, a + b

        n = n + 1

        t=[a,b]

        yield t

    return 'done'

results = []

for n in fib(6):

    print(n)

    results.append(n)

    print(results)


def PascalsTriangle():

    l = [1]

    ll = [1]

    while True:

        yield l

        length = len(l)

        for p in range(1, length):

            ll[p] = l[p - 1] + l[p]

        ll.append(1)

        l = list(ll)











































