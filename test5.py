#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-07-26 13:01:18
# @Last Modified time: 2022-07-26 22:34:41


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


s = [1,2,3,4,5]
s.insert(4,3)



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
    print()
    i += 1



day = 7
hour = 8
while day < 7:
    while hour < 8:
        print('studty hard')
        hour += 1
        if hour > 1:
            break
    day += 1
    


for each in fish:
    print(each)



i = o
while i < len('fish'):
    print('fish'[i])
    i += 1


for i in range(10):
    print(i)




for n in range(2,10):
    for x in range(2,n):
             if n % x == 0:  
                     print(n,'=',x,'*',n//x)
                     break
    else:
                     print(n,'it is a easy number')

rhyme = [three,two,one]
print(rhyme)
for each in rhyme:
    print(rhyme)

s = [1,2,3,4,5]

old = input("please tell me your old:")
old = int(old)

if 0 < old <=18:
    print('teenager')
elif 18 > old > 40:
    print('adult')
elif 40 <= 90:
    print('older')
else:
    print('what')

for i in matrix:
    for each in i:
        print(each,end ='')
        print()





























