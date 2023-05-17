# num = []
# total = 0
# for i in range(1,11):
#     num1 = float(input(f'第{i}位选手的评分：'))
#     num.append(num1)
# print(f'去掉一个最低分{num[0]}')
# print(f'去掉一个最高分{num[len(num)-1]}')
# num.sort()
# num.remove(num[0])
# num.pop()
# for j in num:
#     total += j
# print(f'最终选手得分是：{total/(len(num))}')

# import random
# code_list = []
# for i in range(3):
#     state = random.randint(1,3)
#     if state == 1:
#         first_skill = random.randint(65,90)
#         random_uppercase = chr(first_skill)
#         code_list.append(random_uppercase)
#     elif state == 2:
#         second_skill = random.randint(97,122)
#         random_lower = chr(second_skill)
#         code_list.append(random_lower)
#     elif state == 3:
#         third_skill = random.randint(0,9)
#         code_list.append(str(third_skill))
# total_code = ''.join(code_list)
# print(total_code)
#


# s1 = {1,2,3,4,'牛肝菌'}
# s2 = {100,'我想吃爆炒牛肝菌'}
# s1.add('肋肋姐')
# print(s1)
# s1.remove(1)
# print(s1)
# s1.discard(1)
# print(s1)
# s1.pop()
# print(s1)
# s1.clear()
# print(s1)
# s1.copy()
# print(s1)
# s1.isdisjoint(s2)
# print(s1)


s1 = {'牛肝菌':18,'score':59,'sex':'女'}
s1['杨绿熊'] = 19
print(s1)
print(s1.keys())
print(s1.values())
print(s1.items())
print(s1.get('牛肝菌'))
print(s1.popitem())
print(s1.pop('牛肝菌'))
print(s1.clear())






