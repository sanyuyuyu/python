score , level = input().split()
score = int(score)
if score >= 120 and level == 'A':
	print('通过')
else:
	print('不通过')


N = int(input())
sum_a = 0 
sum_b = 0 
for i in range(n):
	name,group,money = input.split()
	money = int(money)

	if group == 'A':
		sum_a += money 
	elif group == 'B':
		sum_b += money
print(f'A{sum_a}')
print(f'B{sum_b}')
print(f'ALL{sum_a + sum_b}')


