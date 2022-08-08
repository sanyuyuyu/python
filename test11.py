#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-08 15:57:56
# @Last Modified time: 2022-08-08 20:35:30
print(f"wolf wolf")
beautiful = 200
print("{0}".format(beautiful))
print('%.f2' % 3.1415926)

n = 2
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)
    print(n)
   

total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print(total)

import itertools
sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum2+=1
print(sum2)

def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)
print(Fib(int(input())))


 

for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2ld '%(i,j,i*j),end='')
    print()

n = 100
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)































































