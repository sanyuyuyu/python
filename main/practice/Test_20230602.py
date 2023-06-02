print(list(map(lambda x: x * x,[1,2,3,4,5,6,7])))

# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 23:30
# @Author  : 我就是任性-Amo
# @FileName: 33.打印各种图形.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
 
 
# 1.打印矩形
row = int(input("row:"))  # 控制行数
clo = int(input("clo:"))  # 控制每一列星星的个数
for i in range(row):
    print("*" * clo)
 
 
print("------------------------------")
 
 
# 2.打印空心矩形
for i in range(row):
    if i == 0 or i == row - 1:
        print("*" * clo)
    else:
        print("*" + " " * (clo - 2) + "*")
print("------------------------------")
 
 
# 3.打印等腰直角三角形
for i in range(1, row + 1):
    print("*" * i)
print("------------------------------")
 
 
# 4.打印空心等腰直角三角形
for i in range(1, row + 1):
    if i == 1 or i == row:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")
 
 
print("------------------------------")
 
 
# 5.打印等腰三角形 这里的话自定义有点点问题 以后我空了再说
s = 1  # 定义星星的初始个数
for i in range(row + 1):
    if i < row / 2:
        print(" " * ((row - s) // 2) + "*" * s)
    s += 2
 
 
print("------------------------------")
 
 
# # 6.打印右三角形
# for i in range(1, 10):
#     if i >= 6:
#         print("* " * (10 - i))
#     else:
#         print("* " * i)


  
