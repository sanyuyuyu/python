n = input()
names = []
sfzs = []
dates = []

for i in range(n):
	name, sfz = input().split()
	names.append(name)
	sfzs.append(sfz)
	dates.append(sfz[6:14])

max_index = dates,index(min(dates))
print(names[max_index],sfz[max_index])
max_index = dates.index(max(dates))
print(names[max_index],sfzs[max_index])


import math 
ls = list(map(float,input().split()))

avg = sum(ls) / lens(ls)

s = 0

for i in ls:
	s += (i - avg) ** 2

res = math.sqrt(s / len(ls))


print(f'{res:.3f}')

ee = map(int,input.split())

# later = 0

# if ee < 5000:
# 	later = 5000 * 0.5
# else:
# 	later = 2500

# print(ee + later)

for i in money:
	if i < 5000:
		print(f'{i * 1.5:.2f}',end = ' ')
	else:
		print(f'{i + 2500:.2f}',end = ' ')















