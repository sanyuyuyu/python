l = []
n = 1 
while n < 99:
	l.append(n)
	n = n + 2
print(l)

def trim(s):
	if s[0] == '':
		s = trim(s[1:])
	elif s[:-1] == '':
		s = trim(s[:-1])
	else:
		print(s)
s = 'i eat fish'
print(s)
trim(s)