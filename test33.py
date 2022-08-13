#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-10 21:55:54
# @Last Modified time: 2022-08-13 19:49:33

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)
move(3, 'A', 'B', 'C')
