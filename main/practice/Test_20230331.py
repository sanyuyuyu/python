def test(a = 2, b = 4):
	global z
	z += a * b 
	return z
z = 10
print(z,test())

def hub(h,a = 2.0, b = 4.0):
	h += a * h
h = 22
print(h,hub(h,3)) 

a = set('htslbht')
sorted(a)
for i in a:
	print(i,end = '')