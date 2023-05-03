
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = [] 
n = 3
for i in range(n):
	r.append(L[i])
print(r)

def long(self,strs):
	if not strs: return ""
	s1 = min(strs)
	s2 = max(strs)
	for i,x in enumerate(s1):
		if x != s2[i]:
			return s2[:1]
	return s1
	