#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-10 21:55:54
# @Last Modified time: 2022-08-10 22:11:45
height = 1.70
weight = 54
BMI = weight/(height**2)
if BMI < 18.5:
    print('过轻')
elif  BMI >= 18.5 and BMI < 25:
    print('正常')
elif BMI >= 25 and BMI < 28:
    print('过重')
elif BMI >= 28 and BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')

