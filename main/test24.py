#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-26 20:43:01
# @Last Modified time: 2022-08-30 22:10:17
my_list = [1,2,3]
new_list = []
for i in my_list:
    new_list.append(i*2)
print(new_list)

nn_list = [i*2 for i in my_list]
print(nn_list)



nn_list = [i*2 for i in my_list if i > 1]
print(nn_list)



nn_list = [(x,y) for x in range(3) for y in range(3)]
print(nn_list)


nn_list = [(x,y,z,m) for x in range(3) for y in range(3) for z in range(3) for m in range(3)]
print(nn_list)



import time 
def demo1():
    new_list = []
    for i in range(10000000):
        new_list.append(i*2)

def demo2():
    new_list = [i*2 for i in range(10000000)]

s_time = time.perf_counter()
demo2()
e_time = time.perf_counter()
print(e_time-s_time)

x = 6
my_var = [x*2 for x in range(3)]

print(my_var)
print(x)

my_var = [y*4 for y in [x*2 for x in range(3)]]
print(my_var)


my_list = [1,2,3]
new_list = [item * 2 for item in my_list]
print(new_list)

my_list = [1,2,3]
new_list = [item for item in my_list if item >1]
print(new_list)

#{键:值 for 迭代变量 in 可迭代对象 [if 条件表达式]}
my_dict = {key: value for key in range(3) for value in range(2)}
print(my_dict)

my_tuple = (i for i in range(10))
print(my_tuple) #生成器对象


my_set = {value for value in 'hello albb'}
print(my_set) #无序不重复





def even_num(num):
    return True if num % 2 == 0 else False

li = [1,2,4,5,6,7]
ret = [i for i in  li if i % 2 == 0]
ret = [i if i % 2 == 0 else None for i in li]
print(ret)


def max(a, b):
    if a > b:
        ret = a
    else:
        ret = b
    return ret

r = max(3, 4)
print(r)


max = lambda a, b: a if a > b else b
r = max(3,4)
print(r)


num = 22
ret = "xiaoyu20" if num < 20 else ("jishu" if num % 2 == 1 else "oshu")
print(ret)


#元组
age = 18

#(当后面的表达式为假时返回，当后面的表达式为真时返回)[条件表达式]
cn = ("old", "young")[age >= 18]
print(cn)

#字典
age = 18 
cn = {False:"old", True:"young"}[age >= 18]
print(cn)




if __name__ == '__main__':
    pi = [3, 14, 15, 9, 26, 5, 35, 8, 97, 932]
    even_count = 0
 
    for i in pi:
        even_count += 2 if i % 4 == 0 else 1 if i % 2 == 0 else 0
    assert even_count == 6


if __name__ == '__main__':
    pi = [3, 14, 15, 9, 26, 5, 35, 8, 97, 932]
    even_count = 0
    for i in pi:
        even_count += 1 if i % 2 == 0 else 0
    assert even_count == 4


#断言：assert







class Animal:
    def __enter__(self):
        print("__enter__()")

    def __exit__(self, type, value, trace):
        print("__exit__()")


with Animal() as animal:
    pass





import re
 
def naive_calc(code):
    code_lines = [l for l in code.split('\n') if l.strip() != '']
    for line in code_lines:
        ret = re.match("\s*(\d+)([\+\-\*\/])(\d+)\s*", line)
        left = ret.group(1)
        op = ret.group(2)
        right = ret.group(3)
        if op == '+':
            print('{}+{}={}'.format(left, right, int(left)+int(right)))
        elif op == '-':
            print('{}-{}={}'.format(left, right, int(left)-int(right)))
        elif op == '*':
            print('{}*{}={}'.format(left, right, int(left)*int(right)))
        elif op == '/' and right != '0':
            print('{}/{}={}'.format(left, right, int(left)/int(right)))
 
 
def test():
    code = '''
    1+2
    3+4
    5-3
    4*3
    10/2
    '''
    naive_calc(code)
 
 
if __name__ == '__main__':
    test()



my_str = "absdufro"
new_my_str = my_str.title()  #字标索引值
print(new_my_str)
#title 字母开头大写
#lower转小写
#strip 去除左右两端空格
#upper转大写

# my_str.count(sub_str[, start[, end]])

print("abcdesfsw".count('a'))

# my_str.replace(old, new[, count])  old替换为new新字符串

my_str = "i am beautiful"
my_str.split(sep=None, maxsplit=3)
print(my_str)


my_str = 'is it ok ?'
answer_str = "is it ok ?: {}".format("yes.")
print(answer_str)





































































