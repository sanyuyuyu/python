f = abs
print(f(-10))

def add(x,y,f):
	return f(x) + f(y)

num1 = int(input('>>>:'))
ge_wei = num1 % 10
shi_wei = num1 // 10 % 10
qian_wei = num1 // 1000 % 10
wan_wei = num1 // 10000
if ge_wei == wan_wei and shi_wei == qian_wei:
	print(f'{num1}是回文数')
else:
	print(f'{num1}不是回文数')
num2 = input('>>>:')
new_num2 == num2[::-1]
if num2 == new_num2:
	print(f'{num2}是回文数')
else:
	print(f'{num2}不是回文数')
num3 = input('>>>:')
flag = True
for i in range(int(len(num3) / 2)):
	if num3[i] != num3[-i-1]:
		flag = False
		break
if flag:
	print(f'{num3}是回文数')
else:
	print(f'{num3}不是回文数')



