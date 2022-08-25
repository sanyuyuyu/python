#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-25 21:10:32
# @Last Modified time: 2022-08-25 22:13:17


class Names():
    name1='Kevin'
    name2='Tom'
print('hello {names.name1} i am {names.name2}'.format(names=Names))

s = "{:b}".format(8)
print(s) 

s = "{:o}".format(8)
print(s) # 10

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('')

    even = [n for n in list if n % 2 == 0]

    for n in even:
        print(n)

    print('')