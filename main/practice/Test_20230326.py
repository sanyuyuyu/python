import random

brandlist = ['华为', '苹果', '诺基亚', 'OPPO', '小米']

random.seed(0)

name = brandlist[random.randint(0, len(brandlist))]

print(name)

'''
import jieba
s = input("请输入一个字符串：")
n = len(s)
m = len(jieba.lcut(s))
print("中文字符数为：{},中文词数为：{}".format(n,m))
'''
n = eval(input('请输入一个数字:'))

print('{:+^11}'.format(chr(n-1)+chr(n)+chr(n+1)))

import turtle

for i in range(4):
	
    turtle.fd(100)
    turtle.fd(-100)
    turtle.seth((i+1)*90)
