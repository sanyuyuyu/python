# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-30 23:24:20

a = [11,22,45,23,55]

results = {
    'odd':0,
    'even':0
    }

for _ in a:   
    if _ % 2 == 0:
        results['even'] += 1
    else:
        results['odd'] += 1
print(results)

for _ in range(len(a)):
    if a[_] % 2 == 0:
        results['even'] += 1
    else:
        results['odd'] += 1
print(results)

