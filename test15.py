#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-12 13:45:28
# @Last Modified time: 2022-08-12 20:20:14
name=input('请输入你的名字: ')

print('欢迎你',name)

A=input('请输入你的年龄: ')

A=int(A)

if A<18:

    print('你还未成年!')

else:

    print('你已经成年了')

    print('你可以尽情玩游戏!')

    B=input('请输入你想要选择的平台（steam/wegame/手游）: ')

    while B!="steam":

        print('别的有什么好玩的,滚去玩steam!!!')

        B=input('请输入你想要选择的平台（steam/wegame/手游）: ')

    print('欢迎来到steam!')

    D=1

    while D!="0":

        C=input('请选择你要玩的游戏（骑砍/文明）: ')

        if C=="骑砍":

            print('你太菜了，被击杀')

            D=input('是否退出steam?(是0/否1): ')

        elif C=="文明":

            print('你太累了，猝死了')

            D=input('是否选则退出steam? (是0/否1): ')

        else:

            print('找不到对应的游戏，请重新输入')

print('好好学习，天天向上！')





name = input("请输入你的名字：")
sex = input("请输入你的性别：")
age = 18
if age < 18:
    print("未成年不允许进入本游戏。")
else:
    print("欢迎来到王者荣耀！")
    A=input("尊敬的召唤师，请选择模式(无尽模式/大乱斗/排位赛）：")
    while A!="大乱斗":
        print("大乱斗有啥好玩，上分上分！")
        A=input("尊敬的召唤师，请选择模式（无尽模式/大乱斗/排位赛）：")
        print("欢迎来到排位赛！")



import time
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)



high=200
total=100
for i in range(10):
    high/=2
    total+=high
    print(high/2)
print('总长：'，total)




peach=1
for i in range(9):
    peach=(peach+1)*2
print(peach)


































































