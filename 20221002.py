# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-10-02 10:14:45




A=[]
B=[]
a = 'aaa.txt'
with open(a, 'r') as file:
    for line in file:
        print(line)
        b = line.split(',')
        print(b)
        for i in b:
            print(i)
            if int(i) % 2 == 0:
                A.append(int(i))
            else:
                B.append(int(i))

print(sum(A))
print(sum(B))g
