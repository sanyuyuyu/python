#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-15 19:16:49
# @Last Modified time: 2022-09-16 18:46:54
import json
 
file_path = 'test.txt'
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
data_1 = open("奇数行.txt", 'w', encoding='utf-8')
data_2 = open("偶数行.txt", 'w', encoding='utf-8')
 
num = 0  #行数-1
for line in lines:
    if (num % 2) == 0:  #num为偶数说明是奇数行
        print(line.strip(), file=data_1)  # .strip用来删除空行
    else:  
        print(line.strip(), file=data_2)
    num += 1
 
data_1.close()
data_2.close()
 

import json 
if __name__ == '__main__':
    obj = json.loads(json.dumps({"key": {"items": [1, 2, "test"]}}))
    assert obj['key']['items'][2] == 'test'

import os 
path = r'C:/Users/alpha/wss/python/test.txt'
# 分离路径和文件 
a = os.path.split(path) 
print(a)
#分离文件名和后缀
print(os.path.splitext(a[-1]))


import os

























