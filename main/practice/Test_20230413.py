scores = list(map(int, input().split()))
indexes = list(map(int, input().split()))
for index in indexes:
	scores[index - 1] += 10
max_score = max(scores)
res1 = []
res2 = []

for index, score in enumerate(scores):
	if score == max_score:
		res2.append(str(index + 1))
	res1.append(str(score))
print(''.join(res1))
print(''.join(res2))


n = int(input('行李公斤:'))

if n > 10:
	if n <= 20:
		print(n * 2)
	elif n > 20:
		print(n * 3) 


level , product , number = input().split()
number = int(number)

zhekou = 0

if level == '金会员':
	zhekou = 0.85
elif level == '银会员':
	zhekou = 0.9
elif level == '普通会员':
	zhekou = 0.95
else:
	zhekou = 1

mar = 0 

if product == '商品一':
	mar = 100
elif product == '商品二':
	mar = 200
else:
	mar = 300

print(zhekou * mar * number)



M , n = map(int,input().split())

sum = 0

for i in range(M,n+1):
	if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0 :
		sum += i

print(sum)













