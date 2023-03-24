#a和b是两个列表变量,列表a为[3,6,9]已给定,键盘输入列表b,计算a中元素与b中对应元素乘积的累加和
'''
a = [1,2,4] #a列表

b = input("请输出一个数组：") #输入列表b

s = 0 # 设定一个s变量存放累积和

for i in range(len(a)): # 连续输出a，b

	s += a[i] * b[i]    # 累积和

print(s)
'''

#以123为随机数种子,随机生成10个在1(含)到999(含)之间的随机数,每个随机数后跟随——个逗号进行分隔,厅幕输出这10个随机数
import random

 #random.seed(123) 

for i in range(10):

	print(random.randint(1,999),end = ',')


import turtle

turtle.right(-30)
turtle.fd(200)
turtle.right(60)
turtle.fd(200)
turtle.right(120)
turtle.fd(200)
turtle.right(60)
turtle.fd(200)
turtle.right(60)