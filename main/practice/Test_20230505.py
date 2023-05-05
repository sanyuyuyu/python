# print([x * x for x in range(10)])
# print((x * x for x in range(10)))
# def fib(max):
# 	n,a,b = 0,0,1
# 	while n < max:
# 		print(b)
# 		a,b = b,a+b 
# 		n = n + 1
# 	return 'done'
# print(fib(6))

# def odd():
# 	print('step 1')
# 	yield 1
# 	print('step 2')
# 	yield (3)
# 	print('step 3')
	# yield(5)

g = fib(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break