money = map(float,input().split())

for i in money:
	if i < 5000:
		print(f'{i * 1.5:.2f}',end = '')
	else:
		print(f'{i + 2500:.2f}', end = '')


# 第一行为一个正整数n，n100后有n行，每行2个正整数，分别为一名职工测量的收缩压和舒张压，
# 中间以一个空格分隔

n = int(input())

count = 0

for i in range(n):
	a,b = map(int,input().split())
	if 90 <= a <= 140 and 60 <= b <= 90:
		count += 1
print(count)



# n = int(input())

# for i in range(n):
# 	ls = list(map(int,input().split())
# 	l = len(ls)
# 	mx = max(ls)
# 	mn = min(ls)
# 	avg = sum(ls) / len(ls)
# 	print(l, mx, mn, f'{avg:.1f}')



















