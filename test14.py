#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-11 10:56:15
# @Last Modified time: 2022-08-11 19:13:20
a = (1, 2, 3)
dict1 = {'ast': 1, 'abc': 2}
print(dict1)
set1 = {1, 2, 3}
set1.add(a)
print(set1)

b = (1, [2, 3])
print(b)
  
print("\n")



def isLeapYear(y):
    return (y%400==0 or (y%4==0 and y%100!=0))
DofM=[0,31,28,31,30,31,30,31,31,30,31,30]
res=0
year=int(input('Year:'))
month=int(input('Month:'))
day=int(input('day:'))
if isLeapYear(year):
    DofM[2]+=1
for i in range(month):
    res+=DofM[i]
print(res+day)





raw=[]
for i in range(3):
    x=int(input('int%d: '%(i)))
    raw.append(x)
for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)
raw2=[]
for i in range(3):
    x=int(input('int%d: '%(i)))
    raw2.append(x)
print(sorted(raw2))










































