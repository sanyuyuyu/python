# n = int(input())

# count = 0

# for i in range(n):
# 	shou,shu = map(int,input().split())
# 	if 90 <= shou <= 140 and 60 <= shu <= 90:
# 		count += 1 
# print(count)


# a = list(map(float,input().split()))
# for i in a:
# 	if a < 5000:
# 		print(a+a*0.5)
# 	else:
# 		print(a+2500)

# import math


# e = float(input())

# Pi = 0
# start = 1
# flag = 1

# while (4 / start) >= e:
# 	if flag == 1:
# 		Pi += 4/ start 
# 	else:
# 		Pi -= 4/ start
# 	start += 2

# print(Pi)

# print('asdfa')

# # print(math.e)



# m,n = map(int,input().split())

# s = 0
# for i in range(m,n+1):
# 	if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
# 		s += 1
# print(s)

# 0 0 2 2

# [1,2,3]

# numbers = list(map(float,input().split()))

# avg = sum(numbers) / len(numbers)

# p = 0

# for i in numbers:
# 	# what should to do?
# 	p += pow(i - avg, 2)


# s  = p / len(numbers)
# last = pow(s, 1/2)

# print(f'{last:.3f}')





e = float(input())
 
i = 3
s = 4
flag = -1
 
# for循环    while循环
while 4 / (i - 2) >= e:
    s += flag * 4 / i
    i += 2
    flag *= -1
print(f'{s:.5f}')






# e = float(input())

# flag = 1
# pi = 0
# start = 1 
# while (4 / start) > e:
# 	if flag == 1:
# 		pi += 4 / start
# 	else:
# 		pi -= 4 / start 
# 	start += 2
# print(pi)































