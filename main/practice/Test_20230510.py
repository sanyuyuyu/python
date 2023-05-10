# a = [1,2,3,4,5] #列表
# b = {1,2,3,4,5} #集合
# c = (1,2,3,4,5) #元组
# d = {'牛肝菌':90,"乐迪":18,"磊磊姐":19} #字典
# print(a)
# print(b)
# print(c)
# print(d)

# f = 'python'
# print(f[0:6:2])

# list_1 = [1,3,4,52,2]
# print(list_1)
#
# word = 'python'
# print(list(word))  #将字符串转换为列表
#
# word_2 = (1,2,3)
# print(list(word_2)) #将元组转换为列表
#
# for i in list_1: #遍历列表中的元素
#     print(i)
#
# word_3 = [3,2,14,5,71,1]
# print(word_3[0:4:1]) #列表切片
#
# word_4 = [1,2,3]
# word_4[0:2] = [7,5] #列表替换
# print(word_4)


# ls = [5,3,18,9,11]
# ls.sort()
# print(ls)
# ls.reverse()
# print(ls)
# ls[::-1]
# print(ls)
# ls[4:0:-1]
# print(ls)

# score = []
# total_score = 0
# for i in range(1,11):
#     score_1 = float(input(f'第{i}位分数是：'))
#     score.append(score_1)
# score.sort()
# print(f'去掉最低分：{score[0]}')
# print(f'去掉最高分：{score[len(score)-1]}')
# score.remove(score[0])
# score.pop()
# for j in score:
#     total_score += j
# print(f'选手最终得分为：{total_score/(len(score))}')
#
#
# import random
# code_list = []
# for i in range(6):
#     state = random.randint(1,3)
#     if state == 1:
#         first_kind = random.randint(65,90)
#         uppercase = chr(first_kind)
#         code_list.append(uppercase)
#     elif state == 2:
#         second_kind = random.randint(97,122)
#         lowercase = chr(second_kind)
#         code_list.append(lowercase)
#     elif state == 3:
#         third_kind = random.randint(0,9)
#         code_list.append(str(third_kind))
# verification_code = "".join(code_list)
# print(verification_code)




#
# score = []
# total_score = 0
# for i in range(1,11):
#     score1 = float(input(f'第{i}位分数是：\n'))
#     score.append(score1)
# score.sort()
# print(f'去掉最低分{score[0]}')
# print(f'去掉最高分{score[len(score)-1]}')
# score.remove(score[0])
# score.pop()
# for j in score:
#     total_score += j
# print(f'选手的最终得分是：{total_score/(len(score))}')



# import random
# code_list = []
# for i in range(6):
#     state = random.randint(1,3)
#     if state == 1:
#         first_kind = random.randint(65,90)
#         uppercase = chr(first_kind)
#         code_list.append(uppercase)
#     elif state == 2:
#         second_kind = random.randint(97,122)
#         lowercase = chr(second_kind)
#         code_list.append(lowercase)
#     elif state == 3:
#         third_kind = random.randint(0,9)
#         code_list.append(str(third_kind))
# total = "".join(code_list)
# print(total)

# l1 = [1,2,2,3]
# l2 = [i * i for i in l1]
# print(l2)
# l3 = [i * i for i in l2 if i >= 14]
# print(l3)
# l4 = [i + j for i in l1 for j in l2]
# print(l4)

# string = 'python'
# print(string[4:0:-1])
#
# li_num1 = [4,5,2,7]
# li_num2 = [3,6]
# a = li_num2 + li_num1
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)
#
# tu_num1 = ('p','y','t',['o','n'])
#
# str = 'skdaskerkjsalkj'
# count = 0
# for i in str:
#     count += 1
# print(count)

# li_one = [1,2,1,2,3,5,4,3,5,7,4,7,8]
# li_two = []
#
# for i in li_one:
#     for j in li_one:
#         if i == j:
#             li_two.append(i)
#
#
# print(li_two)

# li_one = [1,2,1,2,3,5,4,3,5,7,4,7,8]
# li_two = []



# str = 'skdaskerkjsalkj'
# s_count = 0
# k_count = 0
# d_count = 0
# a_count = 0
# for i in range(len(str)):
#     if str[i] == 's':
#         s_count += 1
#     elif str[i] == 'k':
#         k_count += 1
#     elif str[i] == 'd':
#         d_count += 1
#     elif str[i] == 'a':
#         a_count += 1
# print(f's出现的次数为{s_count}')
# print(f'k出现的次数为{k_count}')
# print(f'd出现的次数为{d_count}')
# print(f'a出现的次数为{a_count}')

# str = 'skdaskerkjsalkj'
 
# for i in str:
#     j=str.count(i)
#     print(i,j)

# str = 'skdaskerkjsalkj'
# c_dict = {}
# strset = set(list(str))
# for each in strset:
#     times = str.count(each)
#     c_dict[each] = times
# print(c_dict)
# str = 'skdaskerkjsalkj'
# dict1 = {}
# for i in str:
#     dict1[i] = str.count(i)
# print(dict1)

tu_num1 = ('p','y','t',['o','n'])
tu_num1[-1].append('h')
print(tu_num1)

li_one = [1,2,1,2,3,5,4,3,5,7,4,7,8]
li_one = list(set(li_one))
print(li_one)
























