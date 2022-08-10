#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-10 21:18:22
# @Last Modified time: 2022-08-10 22:16:21
age = 3
if age <= 18:
    print("you are children")
else:
    print("your are adult")


  
  

s = input('birth: ')
if birth < 2000:
    pritn('非00')
else:
    print('00')

height = 1.75
weight = 80.5
bmi = weight/(height**2)
if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
   
   

birth = input('birth: ')
if birth < 2000:
    print('非00')
else:
    print('00')


for i in range(100,1000):
    s=str(i)
    one=int(s[-1])
    ten=int(s[-2])
    hun=int(s[-3])
    if i == one**3+ten**3+hun**3:
        print(i)








































































