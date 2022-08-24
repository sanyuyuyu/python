#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-24 21:26:49
# @Last Modified time: 2022-08-24 22:30:36


num = input()
ls = []
for i in num:
    ls.append((int(i)+3)%9)
print(f"{ls[2]}{ls[3]}{ls[0]}{ls[1]}")

i = 0
while i < 7:
    i += 1
    if i == 4:
        continue
print(i)

