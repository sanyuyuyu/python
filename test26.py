#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-31 16:34:42
# @Last Modified time: 2022-09-01 18:50:38


#lambda [参数列表]:表达式
fun = lambda x:x+1  #只能有一个表达式   
print(fun(1))


def fun(x):return x+1
print((lambda x:x+1)(1))

#for语句不用在lambda。 只包含一个表达式，不包含复杂语句
lambda a:1 if a > 10 else 0

my_list = [lambda a: a**2, lambda b:b**3]
fun = my_list[1]
print(fun(2))

fun = lambda a: (a+1)**3
print(fun(2))

sorted = lambda *args:None 
x = sorted([3,2,1])
print(x)


my_list = [(1, 2), (3, 1), (4, 0), (11, 4)]
my_list.sort(key=lambda x: x[1])
print(my_list)
#依据第二项排序

def fun(n):
    return lambda x:x+n

new_fun = fun(2)
print(new_fun)



def list_to_dict(list,key_func):
    d = {}
    for item in list:
        k = key_func(item)
        v = item
        list = d.get(k)
        if list is None:
            d[k] = [v]
        else:
            d[k].append(v)
    return d







for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2ld '%(i,j,i*j),end='')
    print()























































