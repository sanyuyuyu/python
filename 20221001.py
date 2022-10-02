# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-10-01 16:03:20


class C:
    def __getitem__(self, index):
        print(index)
c = C()
c[2]
c[2:6]

results = {
    'even':0,
    'odd':0
    }
a = 'aaa.txt'
with open(a, 'r') as file:
    for line in file:
        print(line)
        b = line.split(',')
        print(b)
        for _ in b:
            print(_)
            if int(_) % 2 == 0:
                results['even'] += 1
            else:
                results['odd'] += 1
                
print(results)