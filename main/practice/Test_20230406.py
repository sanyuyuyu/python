a = open('aaa.txt','r')
a.read()
ls = ['12','22','33','44']
f = open('aaa.txt','w')
f = open('aaa.txt','a')
f.write('wss')
print(ls)
f.close()

data = input("请输入姓名: ")
num = 0
age = 0
number = 0
while data:
	num += 1
	infoArr = data.split('')
	age += infoArr([2])
	if infoArr[1] == '男':
		num += 1
	data = input()
age = age / num
print('平均年龄{:.2f},男性人数是{}'.format(age,number))

'''

键盘输入一组人员的姓名、性别、年龄等信息,信息间采用空格分隔,每人一行,空行回车结束录入,示例格式如下:
张三 男 23
李四 女 21
王五 男 18
计算并输出这组人员的平均年龄(保留2位小数)和其中男性人数,格式如下:
平均年龄是20.67 男性人数是2
'''
data = input()

name = 0
male = 0
age = 0
while data:
	


print('平均年龄{:.2f},男性人数是{}'.format())






