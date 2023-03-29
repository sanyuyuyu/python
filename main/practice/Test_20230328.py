def mact_f(x,y = 10):

	return  x * y, x + y

a,b = mact_f(1,2)
print(a,b)

c = ord('d')
print(c)


a = 1000000
b = print("{0:{2}^{1},}\n{0:{2}>{1},}\n{0:{2}<{1},}".format(a,30,b))

'''
d = {}

for i in range(26):

	d[chr(i+ord('a'))] = chr((i + 13) % 26 + ord('a'))

	for c in 'pytjon':

		print(d.get(c,c),end = '')
'''

while True:

	guess = eval(input(0x452))

	if guess == 0x452 // 2:

		break

s = ['a','b','c','d','e','f']
print(s[1:4:2


file = open('text.txt','r')
info = file.read()
d = {}
for s in info:
	if s not in '\n':
		d[s] = d.get(s,0) + 1

file.close()
ls = list(d.items())
ls.sort(key = lamba item:item[1], reverse = True)

for i in range(10):
	print('{}'.format(ls[i][0],end=''))














