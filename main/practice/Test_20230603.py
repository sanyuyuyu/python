# count = 0
# s = 'abcABCa'
# for i in s:
# 	for j in s.lower():
# 		if i == j:
# 			count += 1
# print(count)


# # string = 'Life is short.'
# # a = string.split()
# # for i in a:
# # 	if i == 'python':
# # 		print(a)
# string = 'Life is short. I use python'
# if string.find('python'):
# 	string = string.replace('python','Python')
# 	print(string)
# else:
# 	print(string)

# #静制转换
# a = input('输入要转换的数据：')
# if a == '2':
# 	print(f'{bin(a)}')
# elif a == '8':
# 	print(f'{oct(a)}')
# elif a == '10':
# 	print(f'{int(a)}')
# elif a == '16':
# 	print(f'{hex(a)}')

#输入六位随机数
import random
code_list = []
for i in range(6):
	state = random.randint(1,3)
	if state == 1:
		first_kind = random.randint(65,90)
		uppcase = chr(first_kind)
		code_list.append(uppcase)
	elif state == 2:
		second_kind = random.randint(97,122)
		lower = chr(second_kind)
		code_list.append(lower)
	elif state == 3:
		third_kind = random.randint(0,9)
		code_list.append(str(third_kind))
last = ''.join(code_list)
print(last)




