# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-30 23:24:20

a = [11,22,45,234,55]

results = {
    'odd':0,
    'even':0
    
}

for _ in a:
    print(_)
    if _ % 2 == 0:
        print(_)
        results['even'] += 1
    else:
        results['odd'] += 1
print(results)

for _ in range(len(a)):
    if a[_] % 2 == 0:
        print(_)
        results['even'] += 1
    else:
        results['odd'] += 1
print(results)

