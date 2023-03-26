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


txt = input("请输入类型序列：")
txtArr = txt.split(" ")
d = {}
for item in txtArr:
    d[item] = d.get(item, 0) + 1
ls = list(d.items())
ls.sort(key=lambda item:item[1], reverse=True)
for k in ls:
    print("{}:{}".format(k[0], k[1]))
