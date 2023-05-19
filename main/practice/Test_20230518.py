# for i in range(1,11,2):
# 	print(''* int((9-i) // 2) + '*' * i)
# for j in range(7,0,-2):
# 	print('' * int((9 - j) // 2) + '*' * j)


# from functools import reduce

# num = int(input('请输入num：'))
# get_num = 0
# cheng_ji = 1
# for j in range(1,num+1):
# 	cheng_ji *= j 
# 	get_num += cheng_ji
# print(f'1+2!+3+...+{num}!={get_num}')

# L = range(1,num+1)
# def operate(x):
# 	r = 1
# 	for i in range(1,x + 1):
# 		r *= i # s = sum(mao(operate,L))
# print(f'1+2!+3+...+{num}!={get_num}')

def fact(num):
	if num == 1:
		return 1 
	else:
		return num * fact(num - 1)
print(fact(5))
