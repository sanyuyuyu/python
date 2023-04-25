#1.使用字符串的格式化输出完成以下名片的显示
#3.编程实现：用户在键盘中输入自己的名字，例如“张三”，终端打印“你好，张三”

# name = input()
# print('你好，张三')

#4.判断下面的代码是否写的正确，如果不正确，请修改代码，然后执行代码。

#5.编写程序，从键盘获取用户名和密码，然后判断，如果正确就输出以下信息: "欢迎来到博学谷！"
# name = input('姓名：')
# password = input()
# if name == 'zs' and password == '123456':
# 	print('欢迎来来到博学谷')

#6.编写代码设计简易计算器，可以进行基本的加减乘除运算。
# a = int(input('请输入一个数字：'))
# b = int(input('请输入另一个数字：'))
# c = input('请输入运算符：')
# if c == '+':
#     print(a+b)
# elif c == '-'
#     print(a-b)
# elif c == '/':
#     print(a/b)

#7.考试成绩的问题：提示用户输入成绩，判断是属于哪个水平，
# 将结果打印到控制台。60以下不及格，60分以上为及格
# 70分至80分为合格，80分至90分为良好，90分以上为优秀。
# score = float(input())
# if score < 60:
#     print('不合格')
# elif score == 60:
#     print('及格')
# elif 70 <= score <= 80:
#     print('合格')
# elif 80 <= score <= 90:
#     print('良好')
# else:
#     print('优秀')

#8. 使用while打印如下图形
# num = 1
# flag = 1
# while num > 0:
# 	print('*'*num)
# 	if num == 5:
# 		flag = False
# 	if flag:
# 		num += 1
# 	else:
# 		num -= 1

#9.使用for循环，依次打印字符串"abcdef"中的每个字符。
# a = 'abcdef'
# for i in a:
#     print(i)

#10.请将a字符串反转并输出。例如：'abc'的反转是'cba'
# a = 'abc'
# b = a[::-1]
# print(b)

#11.把[1,2,3,4]转换成"1234"
# lst = [1,2,3,4]
# print(lst)

#12.编程实现 把一个元素全为数字的列表中的所有偶数加1
# a = [1,2,3,4,5,6,7,8]
# s = 0
# while s < len(a):
#     if a[s] % 2 == 0:
#         a[s] += 1
#     s+= 1
# print(a)


#13. test = ("a","b","c","a","c") ，
#统计元祖中每个元素出现的次数把最终的结果保存到列表中，例如[('a',1),('b',3),('c',5)]。
#test = ("a","b","c","a","c")


'''在控制台输入 3 组个人信息，每个人有姓名和年龄，将信息存入字典中，将字典存入列表。

 遍历列表，打印每个人的信息，打印格式如下：

	1 张三 20

	2 李四 22

	3 王五 23
'''

'''
15.已知字符串 test = "aAsmr3idd4bgs7Dlsf9eAF",将字符串中的数字取出，生成一个新的字符串

'''
# test = "aAsmr3idd4bgs7Dlsf9eAF"

# s = ''

# for i in test:
# 	if s == '0123456789':
# 		s += i
# print(s)

#16.现有字符串 msg = "hel@#$lo pyt \nhon ni\t hao%$" ，
#去掉所有不是英文字母的字符，打印结果："请理以后的结果为：hellopythonnihao"
# msg = "hel@#$lo pyt \nhon ni\t hao%$"

# s = ''
# for i in msg:
# 	if i == '@#%$':
# 		s += i 
# print(s)

'''
定义函数findall，要求返回符合要求的所有位置的起始下标，
如字符串"helloworldhellopythonhelloc++hellojava"，

需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)

'''

# def findall(src,dst):
# 	lg = len(dst)
# 	res = []
# 	for index in range(lg):
# 		if src[index:index+lg] == dst:
# 			res.append(index)

'''
定义一个函数 sum_test 接收一个参数 n ，在函数中计算 1 + 2 + 3 + ... + n 的值，并打印结果。

'''
'''
使用不定长参数定义一个函数max_min，接受的参数类型是数值，最终返回这些数中的最大值和最小值

'''
'''
把一个文件中的内容，复制到另外一个文件中。

'''

class Fruit():
	def __init__(self,fruit_type):
		self.type = fruit_type
		self.color = None
		self.price = None
	def Set_color(self,color):
		self.color = color
	def Set_price(self,price):
		self.price = price
	def __str__(self):
		if self.color is None or self.price is None:
			return '水果价格和颜色没有设置'
		else:
			return f'{self.type}:color--{self.color} price--{self.price}元'
apple = Fruit('苹果')
apple.Set_color('red')
apple.Set_price(5)
print(apple)




















