# num = input('请输入数字：')
# count = int('请输入相加的个数：')
# get_sum = 0
# str_list = [] 
# for i in range(1,count+1):
# 	str_list.append(str(num * i))
# 	get_sum += int(num * i)
# print(f"{get_sum}={'+'.join(str_list)}")


for i in range(1,1000):
	num_list = []
	for k in range(1,i):
		if i % k == 0:
			num_list.append(k)
	if sum(num_list) == i:
		str1 = '+'.join(map(str,num_list))
		print(f'{i}={str1}')
