#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-07-26 13:01:18
# @Last Modified time: 2022-07-26 15:11:24


i = 0
while i < 10:
    i +=1
    if i % 2 == 0:
             continue
    print(i)


i = 1
while i < 5:
    print('ok')
    i += 1
else:
    print('no')


i = 1
while i < 5:
    print('yes')
    if i == 2:
        break
    i += 1
else:
    print('no')




day = 1
while day <= 7:
    answer = input('did you have a good work')
    if answer != 'yes ':
        break
    day += 1
else:
    print('you are a good job')


i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, "*", i, "=", j * i, end=" ")
        j += 1
    print（）
    i += 1























































