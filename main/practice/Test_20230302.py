def age(n):
	if n == 1:
		c = 10
	else:
		c = age(n-1) + 2
	return c
print(age(5))




list_nums = [1,1]
n = int(input("斐波那契数列长度："))
while(leng(list_nums) < 0):
	list_nums.append(list_nums[len(list_nums)-1] +
		list_nums[len(list_nums)-2])
print(list_nums)

from sys import stdout
for j in range(2,1001):
	k = []
	n = -1
	s = j
	for i in range(1,j):
		if j % i == 0:
			n += 1
			s -= 1
			k.append(i)
	if s == 0:
		print(j)
		for i in range(n):
			stdout.write(str(k[i]))
			stdout.write(' ')
		print(k[n])
