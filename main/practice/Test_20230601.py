test = ('a','b','c','d')
temp = []
for i in test:
	if i not in temp:
		temp.append(i)
result = [(i,test.count(i)) for i in temp]
print(result)

i = 1
while i <= 12:
    if i == 6 or i == 10:
        i += 1
        continue
    if i == 12:
        print(i, end="")
    else:
        print(i, end=",")
    i += 1
print()
print("***************************")
# 2.使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
j = 100
while j >= 50:
    print(j)
    if j == 50:
        k = 0
        while k <= 50:
            print(k)
            k += 1
    j -= 1
print("***************************")
# 或者直接使用第二种方法:
count = 100
while count > -2:
    if count >= 50:
        print(count)
    else:
        print(49 - count)
    count -= 1
print("***************************")
# 3.使用 while 循环实现输出 1-100 内的所有奇数
m = 1
while m <= 100:
    if m % 2 != 0:
        print(m)
    m += 1
print("***************************")
# 4.使用 while 循环实现输出 1-100 内的所有偶数
n = 1
while n <= 100:
    if n % 2 == 0:
        print(n)
    n += 1
print("***************************")
# 5.使用while循环实现输出2-3+4-5+6…+100 的和
j = 2
get_sum = 0
while j <= 100:
    if j % 2 != 0:
        get_sum -= j
    else:
        get_sum += j
    j += 1
 
 
print(get_sum)