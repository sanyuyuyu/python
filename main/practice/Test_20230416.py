n = int(input())

for i in range(n):
	ls = list(map(int,input().split()))
	l = len(ls)
	mx = max(ls)
	mn = min(ls)
	avg = sum(ls) / len(ls)
	print(l,mx,mn,f'{avg:1f}')

s = int(input())

if 3 <= s <= 5:
	print('春季')
elif 6 <= s <= 8:
	print('夏季')
elif 9 <= s <= 11:
	print('秋季')
else:
	print('冬季')

a,b,c = map(int,input().split())


if a > 100:
	print('A货物库存高了')
if b > 200:
	print('B货物库存高了')
if c > 220:
	print('C货物库存高了')
if a <= 100 and b <= 200 and c<= 200:
	print('检查正常')

g = int(input())
sum = 1
for i in range(n+1):
	if i % 2 == 1:
		sum += i
print(sum)


all = int(input())

if all < 60000:
	print(all)
set = all - 60000
if set < 36000:
	print(all - set * 0.03 )
elif 140000 > set > 36000:
	print(all - 36000 * 0.03 - (set - 36000) * 0.1)
elif 140000 < set <= 300000:
	print(all - 36000 * 0.03 - (144000 - 36000) * 0.1 - (set - 144000) * 0.2)
else:
	print(all - 36000 * 0.03 - (144000 - 36000) * 0.1 - (300000 - 144000) * 0.2 - (set - 300000) * 0.25)


ss = map(str,input().split())

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for i in range(ss):
	if A in ss:
		sum1 += i
		print(f'A选项{sum1}个')
	if B in ss:
		sum2 += i
		print(f'B选项{sum2}个')
	if C in ss:
		sum3 += i
		print(f'C选项{sum3}个')
	if D in ss :
		sum4 += i
		print(f'D选项{sum4}个')





answer = input().split()
 
count_a = answer.count("A")
print(f'A选项{count_a}个')
count_b = answer.count("B")
print(f'A选项{count_b}个')
count_c = answer.count("C")
print(f'A选项{count_c}个')
count_d = answer.count("D")
print(f'A选项{count_d}个')














