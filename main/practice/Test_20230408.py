s = 0
def fun(num):
	try:
		s += num
		return 3
	except:
		return 0
		return 5
print(fun(2))
'''

def fun1():
	print(' in fun1()')
	fun2()
	fun1()
def fun2():
	print('in fun2()')
	fun1()
	fun2()
A. in fun1()

in fun2()

'''


def test( b = 2, a = 4):
	global z
	z += a * b
	return z
	z = 10
	print(z, test())


def hub(ss,x = 2.0,y = 4.0):
	ss += x * y 
	ss = 10
	print(ss,hub(ss,3))


img1 = [12,34,56,78]
img2 = [1,2,3,4,5]
def displ():
	print(img1)
def modi():
	img1 = img2
modi()
displ()

















