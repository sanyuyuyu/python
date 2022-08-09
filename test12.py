#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-09 10:52:46
# @Last Modified time: 2022-08-09 19:01:40
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2ld '%(i,j,i*j),end='')
    print()

for i in range(100,1000):
    s=str(i)
    one=int(s[-1])
    ten=int(s[-2])
    hun=int(s[-3])
    if i == one**3+ten**3+hun**3:
        print(i)






import datetime
print(datetime.date.today())
print(datetime.date(2333,2,3))
print(datetime.date.today().strftime('%d/%m/%Y'))
day=datetime.date(1111,2,3)
day=day.replace(year=day.year+22)
print(day)



string=input("输入字符串：")
alp=0
num=0
spa=0
oth=0
for i in range(len(string)):
    if string[i].isspace():
        spa+=1
    elif string[i].isdigit():
        num+=1
    elif string[i].isalpha():
        alp+=1
    else:
        oth+=1
print('space: ',spa)
print('digit: ',num)
print('alpha: ',alp)
print('other: ',oth)

















































































