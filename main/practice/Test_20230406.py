a = open('aaa.txt','r')
a.read()
ls = ['12','22','33','44']
f = open('aaa.txt','w')
f = open('aaa.txt','a')
f.write('wss')
print(ls)
f.close()

data = input("请输入姓名")
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