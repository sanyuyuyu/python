'''
s = input('行李重量：')
 
sum = 0
if s > 10:
	print('需办理托运')
elif s > 10 and s <= 20:
	sum = (s - 10) * 2 
elif s > 20:
	sum = s * 3 
print(sum)


n = int(input())

if n <= 10:
	print(0)
elif n <= 20:
	print(n * 2)
else:
	print(n * 3)
'''

level, product , number = input().split()
number = int(number)

zhekou = 0

if level == '金会员':
	zhekou = 0.85
elif level == '银会员':
	zhekou = 0.9
elif level == '普通会员':
	zhekou = 0.95
else:
	zhoukou = 1

danjia = 0 

if product == '商品一':
	danjia = 100
elif product == '商品二':
	danjia = 200
elif product == '商品三':
	danjia = 300

print(int(danjia * number * zhekou))


n = int(input())

if n < 10:
	print(n * 10)
else:
	print(n * 9)



n = int(input())

for i in range(30):
	if str(n) == str(n)[::-1]:
		print(i)
		break
	else:
		n = n + int(str(n)[::-1])
else:
	print(30)















