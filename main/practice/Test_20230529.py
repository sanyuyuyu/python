# print(sorted([34,-1,32,4,1],key = abs))
# print(sorted(['abs','shid','djp']))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return sorted(L,key = lambda x:x[0])
def by_score(t):
	return sorted(L,key = lambda x:x[1],reverse=True)
t = L 
a = by_name
b = by_score
print(a)
print(b)


