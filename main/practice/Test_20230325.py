#键盘输入一组人员的姓名、性别、年龄等信息,信息间采用空格分隔,每人一行,空行回车结束录入

data = input()

num = 0

age = 0

male = 0

while data:

	num += 1

	infoArr = data.split('')

	age += int(infoArr[2])

	if infoArr[1] == '男':
		
		num += 1

		data = input()

	age = age / num

print('平均年龄{:.2f},男性人数是{}'.format(age,male))


file = open("命运.txt", "r", encoding="utf-8")

info = file.read()

d = {}

for s in info:

    if s not in "，。？《》！【】“”‘’、":

        d[s] = d.get(s, 0 ) + 1

arr = list(d.items())

arr.sort(key=lambda item:item[1], reverse=True)

file.close()

print("{}:{}".format(arr[0][0],arr[0][1]))
