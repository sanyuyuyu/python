# import random
# total = []
# for i in range(6):
#     state = random.randint(1,3)
#     if state == 1:
#         first_total = random.randint(65,90)
#         random_uppercase = chr(first_total)
#         total.append(random_uppercase)
#     elif state == 2:
#         second_total = random.randint(97,120)
#         random_lower = chr(second_total)
#         total.append(random_lower)
#     elif state == 3:
#         third_total = random.randint(0,9)
#         total.append(str(third_total))
# last = "".join(total)
# print(last)


# num = []
# total = 0
# for i in range(1,11):
#     num1 = float(input(f'第{i}位选手得分：\n'))
#     num.append(num1)
# num.sort()
# print(f'去掉最低分{num[0]}')
# print(f'去掉最高分{num[len(num) - 1]}')
# num.pop()
# num.remove(num[0])
# for j in num:
#     total += j
# print(f'选手最终得分是：{total/len(num)}')


player_info = {}
li = []
print('输入quit表示选手成绩录入完毕')
while True:
    name = input("请输入选手名称：\n")
    if name == 'quit':
        break
    score = float(input('qi请输入选手票数：\n'))
    player_info[name] = score
items = player_info.items()
for j in items:
    li.append([j[1],j[0]])
li.sort()
count = len(li) - 1
for i in range(1,len(li) + 1):
    print(f'第{i}名：{li[count][1]},成绩为{li[count][0]}分')
    count -= 1
