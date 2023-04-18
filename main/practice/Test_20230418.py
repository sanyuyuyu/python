n = int(input())
sum1 = 0
sum2 = 0

for i in range(n):
	name,list,sum = input.split()
	money = int(money)
	if list == 'A':
		sum1 += money
	else:
		sum2 += money
print(sum1) 
print(sum2)
print(sun1+sum2)


m = float(input())

if m < 2000:
	print('*')
elif 2000 <= m < 3000:
	print('**')
elif 3000 <= m < 4000:
	print('***')
elif 4000 <= m < 5000:
	print('****')
elif 5000 <= m:
	print('*****')



def test(s):
	a = str(s)
	step = 0
	while a != a[::-1]:
		a = int(a) + int(a[::-1])
		a = str(a)
		step += 1
		if step > 30:
			return step
print(step)




g = int(input())

for i in range(g):
	if str(g) == str(g)[::-1]:
		print(i)
		break
	else:
		n = n + int(str(n)[::-1])
else:
	print(30)


















































