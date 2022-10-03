# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-10-03 13:38:07
def main():
    file = open('aaa.txt','r')
    lines = file.readlines()
    return lines
    list_name = []
    list_age = []
    list_height = []
    for line in lines:
        elements=line.split()
        ist_name.append(elements[0])

        list_age.append(elements[1])

        list_height.append(elements[2])

    a = 0
    b = 0 
    c = 0 

    for i in range(len(list_age)):
        if a < 20:
            print(a)
main()







a = ('zhangsan', 16, 80)

dict2 = {'name': 'zhangsna', 'age':18, 'height': 80}
print(dict2)

b = ('zhaoliuqi', 19, 84) n    
dict3 = {'name': 'zhaoliuqi', 'age': 19, 'height': 84}
print(dict3)


























