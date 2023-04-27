# a = 20
# b = 30
# # a = a ^ b
# # b = a ^ b
# # a = a ^ b
# # print(f'变量交换之后的a的值为{a},b的值为{b}')

# a = a + b 
# b = a - b
# a = a - b
# print(f'变量交换之后的a的值为{a},b的值为{b}')


# x = int(input('>>>:'))
# y = int(input('>>>:'))
# z = int(input('>>>:'))

# num_list = [x,y,z]
# num_list.sort()
# print(num_list)




# def fibonacci1(n):
# 	a = 0 
# 	b = 0 
# 	for i in range(n):
# 		a,b = b, a+b
# 	print(f'斐波那契数列第{n}项的值为:{a}')
# fibonacci1(3)


# def fibonacci2(n):
# 	if n == 1 or n == 2:
# 		return 1
# 	else:
# 		return fibonacci2(n-1) + fibonacci2(n - 2)
# print(fibonacci2(10))


def fibonacci3(n):
	fibs = [1,1]
	if n == 1:
		return [1]
	if n == 2:
		return [1,1]
	for i in range(2,n):
		fibs.append(fibs[-1] + fibs[-2])
	return fibs
print(fibonacci3(10))






