def fibonacci4(n):
	a = 0 
	b = 1 
	for i in range(0,n):
		a,b = b,a+b 
		yield a 
		print('amo')
f = fibonacci4(4)
print(f)
print(next(f))
print(f.__next__)

list1 = [1,2,3,4,5]
print(list1)
new_list1 = list1.copy()
print(new_list1)