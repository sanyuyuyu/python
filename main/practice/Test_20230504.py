# list(range(1,11))
# L = []
# for x in range(1,11):
# 	L.append(x * x)
# print(L)
# q = [x * x for x in range(1,11)]
# print(q)
# a = [m + n for m in 'ABC' for n in 'XYZ']
# print(a)


# import os
# s = [d for d in os.listdir('.')]
# print(s)

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k,v in d,items():
# 	print(k,'=',v)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

print([x for x in range(1,11) if x % 2 == 0])

# print([x for x in range(1,11) if x % 2 == 0 else 0])

print([x if x % 2 == 0 else -x for x in range(1,11)])

x = 'abc'
y = 123
print(isinstance(x,str))