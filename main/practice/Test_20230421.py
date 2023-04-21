# n = int(input())
# name = []
# number = []
# date = []
# for i in range(n):
# 	name , number = input().split()
# 	name.append(name)
# 	number.append(number)
# 	date.append(number[6:14])
# max = date.index(min(date))
# min = date.index(max(date))
# print(name[max],number[max])
# print(name[min],number[min])
# n = int(input())
 
 
# names = []
# sfzs = []
# dates = []
 
# for i in range(n):
#     name, sfz = input().split()
#     names.append(name)
#     sfzs.append(sfz)
#     dates.append(sfz[6:14])
 
# max_index = dates.index(min(dates))
# print(names[max_index], sfzs[max_index])
# min_index = dates.index(max(dates))
# print(names[min_index], sfzs[min_index])


# number = list(map(float,input().split()))
# avg = sum(number) / len(number)
# p = 0
# for i in number:
# 	p += pow(i-avg,2)
# g = p / len(number)
# s = pow(g,1/2)
# print(f'{s:.3f}')


# n = int(input())

# shou = 0
# shu = 0
# s = 0
# for i in range(n):
# 	shou,shu = map(int,input().split())
# 	if 90 <= shou <= 140 and 60 <= shu <= 90:
# 		s += 1

# print(s)


# rare = list(map(float,input().split()))

# for i in rare:
# 	if i < 5000:
# 		print(f'{i * 1.5:.2f}',end = '')
# 	else:
# 		print(f'{i + 2500:.2f}',end = '')


# n = input()

# if n[0] == 'A':
# 	print('西门')
# if n[0] == 'B':
# 	print('西门')
# if n[0] == 'C':
# 	print('西门')
# else:
# 	print('东门')

# n = list(map(int,input().split()))

# max = [] 
# min = []
# for i in n:
# 	if i > i + 1:
# 		max = i 
# 	print(max)
# 	if i < i + 1:
# 		min = i 


# n = int(input())

# for i in range(n):
# 	ls = list(map(int,input().split()))
# 	mx = max(ls)
# 	mn = min(ls)
# 	l = len(ls)
# 	avg = sum(ls) / len(ls)
# 	print(l,mx,mn,f'{avg:.1f}')

# year , time = map(int,input().split())

# if year >= 5:
# 	if time > 40:
# 		print(f'{50 * 40 + (time - 40) * 50 * 1.5 :.2f}')
# 	else:
# 		print(f'{time * 50 :.2f}')
# else:
# 	if time > 40:
# 		print(f'{30 * 40 + (time - 40) * 1.5 :.2f}')
# 	else:
# 		print(f'{time * 30 :.2f}')



# pi = input()

# p = 0
# start = 1
# if 4 / start > e:
# 	p += 4 / start 
# 	break
# elif:
# 	p -= 4 / start


# e = float(input())

# i = 3
# s = 4
# flag = -1

# while 4 / (i - 2) >= e:
# 	s += flag * 4 / i 
# 	i += 2
# 	flag *= -1
# print(f'{s:.5f}')

# n = input()

# if int(n[:-1]) % 2 == 0:
# 	print('B')
# else:
# 	print('A')


# n = int(input())
# if 3 <= n <= 5:
# 	print('春季')
# elif 6  <= n <= 8:
# 	print('夏季')
# elif 9 <= n <= 11:
# 	print('秋季')
# else:
# 	print('冬季')


# A,B,C = map(float,input().split())

# if A >= 100:
# 	print('A货物库存高了')
# if B >= 200:
# 	print('B货物库存高了')
# if C >= 220:
# 	print('C货物库存高了')
# if A < 100 and B < 200 < C < 220:
# 	print('检查正常')

# n = int(input())
# num = 1
# for i in range(1,n + 1):
# 	if i % 2 != 0:
# 		num *= i 
# print(num)

# #
# n = input().split()

# a = n.count('A')
# print('A选项有{}'.format(a))
# b = n.count('B')
# print('B选项有{}'.format(b))
# c = n.count('C')
# print('C选项有{}'.format(c))
# d = n.count('D')
# print('D选项有{}'.format(d))


# n = input().split()

# if int(n[0]) > 120 and n[1] == 'A':
# 	print('通过') 


# n = int(input())

# sum_a = 0
# sum_b = 0

# for i in range(n):
# 	name , rank, money = input().split()
# 	money = int(money)
# 	if rank == 'A':
# 		sum_a += money
# 	else:
# 		sum_b += money 
# print(f'A{sum_a}')
# print(f'B{sum_b}')
# print(f'ALL{sum_a+sum_b}')

# n = int(input())
# score = list(map(int,input().split()))
# score.remove(max(score))
# score.remove(min(score))
# last_score = sum(score) / len(score)
# print(f'{last_score:.2f}')



# a,b = map(int,input().split())
# s = 0
# if a >= b:
# 	a,b = b,a
# for i in range(a,b+1):
# 	if i % 2 == 0:
# 		s += i
# print(s)


# n = input()
# if len(n) >= 8:
# 	print('True')
# else:
# 	print('False')



# n = int(input())
# age , score = map(int,input.split())
# s_1 = 0
# for i in range(n):
# 	if age >= 35:
# 		if score >= 80:
# 			print('晋升')
# 			s_1 += 1
# 		else:
# 			print('原岗')
# 	if age < 35:
# 		if score >= 90:
# 			print('晋升')
# 			s_2 += 1
# 		else:
# 			print('原岗')

# print(s_1+s_2)






# n = int(input())

# count = 0 

# for i in range(n):
# 	age , score = map(int,input().split())

# 	if (age >= 35 and score >= 80) or (age < 35 and score >= 90):
# 		count += 1
# 		print('晋升')
		
# 	else:
# 		print('原岗')

# print(count)


# n = input()
# if int(n[3:]) == 3:
# 	print('三等奖')
# elif int(n[2:]) == 25:
# 	print('二等奖')
# elif int(n[1:]) == 618:
# 	print('一等奖')
# elif int(n) == 2166:
# 	print('特等奖')


# 第一种方式
# score = input().split()     #默认空格分割成字符串元素的列表
# score = [int(i) for i in score]    #将字符串元素列表转换成整数元素的列表，分数score
 
# 第二种方式
# map对象--->list对象，map对象可以用来做循环遍历，但是不能拿它里面每一个元素的值
# 如果需要拿它里面的值可以强制类型转换为list，list对象    
scores = list(map(int, input().split()))                #使用map映射函数
 
indexes = list(map(int, input().split()))
 
for index in indexes:
    scores[index - 1] += 10
 
#找出总分最高的选手
max_score = max(scores)      #找出了最高分
# score.index(max_score)      #这种方法有一个弊端就是只能找到第一个最高分所在的下标，不符合题目要求
 
# 第一种方式
res1 = []
res2 = []
for index, score in enumerate(scores):
    if score == max_score:
        res2.append(str(index + 1))
    res1.append(str(score))
print(' '.join(res1))
print(' '.join(res2))
 
 
# 第二种方式
#res = []
#for i in range(len(scores)):
#    if(scores[i] == max_score):
#        res.append(index + 1)
#print(' '.join(res))
 
 












