# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-10-04 20:02:12

with open('aaa.txt', 'r') as file:
    for line in file:
        print(line)

a = ('张三', 16, 80)

dict2 = {'name': '张三', 'age':16, 'height': 80}
print(dict2)

b = ('赵六七', 19, 84) 
dict3 = {'name': '赵六七', 'age': 19, 'height': 84}
print(dict3)
