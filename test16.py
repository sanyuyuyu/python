#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-13 11:36:42
# @Last Modified time: 2022-08-13 19:12:36
PI = 3.14159265453
r = float(input('请输入您所求圆的半径：'))
def area_of_circle(r):
    if r <= 0:
        return None
    else:
       return PI*r**2

s = area_of_circle(r)


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x







import math

def quadratic( a , b , c ) :
    if not isinstance( a * b * c ,( int , float )) :
        raise TypeError('输入格式错误')
    q = b * b - 4 * a * c
    if q < 0 :
        print('此方程无解')
    elif q == 0 :
        print('此方程解唯一')
        x = ( -b ) / ( 2 * a )
        return x
    else :
        x1 = ( ( -b + math.sqrt( q ) ) / ( 2 * a ) )
        x2 = ( ( -b - math.sqrt( q ) ) / ( 2 * a ) )
        return  x1 , x2
print('ax^2 + bx + c = 0 , 输入abc的值计算方程的解')
A = input('请输入a的值')
B = input('请输入b的值')
C = input('请输入c的值')
a = int(A) or float(A)
b = int(B) or float(B)
c = int(C) or float(C)
print( a , 'x^2 +' , b , 'x +' , c , '= 0 的解为' , quadratic( a , b , c ))













