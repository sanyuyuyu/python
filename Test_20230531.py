# #十佳歌手
# score = []
# total = 0
# for i in range(1,11):
#     score1 = float(input(f'第{i}位选手的分数是:\n'))
#     score.append(score1)
# score.sort()
# print(f'去掉最低分{score[0]}')
# print(f'去掉最高分{score[len(score) - 1]}')
# score.pop()
# score.remove(score[0])
# for j in score:
#     total += j
# print(f'该选手最终获得的分数是{total / len(score)}')
#


# play = {}
# li = []
# print('输入quit表示该选手成绩录入完毕')
# while True:
#     name = input('请输入选手名称：\n')
#     if name == 'quit':
#         break
#     score = input('请输入选手票数：\n')
#     play[name] = score
# items = play.items()
# for j in items:
#     li.append([j[1], j[0]])
# li.sort()
# count = len(li) - 1
# for i in range(1, len(li) + 1):
#     print(f'第{i}名：{li[count][1]},成绩为{li[count][0]}分')
#     count -= 1

#1到100的和
# def sum(c):
#     for i in range(1,101):
#         c += i
#     print(c)
# sum(0)
#1821到2021年闰年个数print出来
# def is_leap(begin,end,year):
#     leap = False
#     leap = (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
#     return leap
# is_leap(1821,2021,4)
#
# def sum(begin,end,count = 0):
#     for year in range(begin,end+1):
#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             print(f'{year}是闰年')
#             count += 1
#     print(count)
# sum(1821,2021,count = 0)






#1-1000的同位数

def same(a,b):
    for i in range(a,b):
        if ((i / 100) ** 3 + (i % 10) ** 3 + ((i % 100) / 10) ** 3) == i:
            print(f'{i}是水仙数')
same(1,1000)




















