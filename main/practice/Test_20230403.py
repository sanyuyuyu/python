a = [2,3,4]
b = eval(input('请输入一个整数:'))
s = 0
for i in range(len(a)):
	s += a[i] * b[i]
print(s)

import random
random.seed(3)
for i in range(10):
	print(random.randint(1,999),end='')