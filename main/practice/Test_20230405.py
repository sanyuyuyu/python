

a = int(input('工资'))

tax = 0

if a <= 60000:
	print(a)
else:
	tax = a - 60000
	if tax <= 36000:
		print(int(a - tax * 0.03))
	elif tax <= 144000:
		print(int(a - 36000 * 0.03 - (a - 36000) * 0.1))
	elif tax <= 300000:
		print(int(a - 36000 * 0.03 -(144000 - 36000) * 0.1 - (a - 144000) * 0.2))
	else:
		print(int(a - 36000 * 0.03 - (144000 - 36000) * 0.1 - (300000 - 144000) * 0.2 - (a - 300000) * 0.25))

