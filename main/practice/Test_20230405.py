
ss =input().split()

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for i in ss:
	if 'A' in ss:
		sum1 += i
		print(sum1)
	if 'B' in ss:
		sum2 += i
		print(sum2)
	if 'C' in ss:
		sum3 += i
		print(sum3)
	if 'D' in ss :
		sum4 += i
		print(sum4)
#
# answer = input().split()
#
# count_a = answer.count("A")
# print(f'A选项{count_a}个')
# count_b = answer.count("B")
# print(f'A选项{count_b}个')
# count_c = answer.count("C")
# print(f'A选项{count_c}个')
# count_d = answer.count("D")
# print(f'A选项{count_d}个')