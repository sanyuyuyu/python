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

#
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

#
# player_info = {}
# li = []
# print('输入quit表示选手成绩录入完毕')
# while True:
#     name = input("请输入选手名称：\n")
#     if name == 'quit':
#         break
#     score = float(input('qi请输入选手票数：\n'))
#     player_info[name] = score
# items = player_info.items()
# for j in items:
#     li.append([j[1],j[0]])
# li.sort()
# count = len(li) - 1
# for i in range(1,len(li) + 1):
#     print(f'第{i}名：{li[count][1]},成绩为{li[count][0]}分')
#     count -= 1


person_info = []
print('=' * 20)
print('欢迎使用通讯录:')
print('1.添加联系人')
print('2.查看通讯录')
print('3.删除联系人')
print('4.修改联系人信息')
print('5.查找联系人')
print('6.退出')
print('=' * 20)
while True:
    per_dict = {}
    fun_num = input('请输入功能序号：')
    if fun_num == '1':
        per_name = input('请输入联系人的姓名：')
        phone_name = input('请输入联系人的手机号：')
        per_email = input('请输入联系人的邮箱：')
        per_address = input('请输入联系人的地址：')
        if per_name.strip() == '':
            print('请输入正确信息')
            continue
        else:
            per_dict.update({'姓名': per_name,
                             '手机号': phone_name,
                             '电子邮箱': per_email,
                             '联系地址': per_address})
            person_info.append(per_dict)
            print('保存成功')
    elif fun_num == '2':
        if len(person_info) == 0:
            print('通讯录无信息')
        for i in person_info:
            for title,info in i.items():
                print(title + ':' + info)
    elif fun_num == '3':
        if len(person_info) != 0:
            del_name = input('请输入要删除的联系人姓名：')
            for i in person_info:
                if del_name in i.values():
                    person_info.remove(i)
                    print(person_info)
                    print('删除成功')
                else:
                    print('该联系人不在通讯录中')
        else:
            print('通讯录无信息')
    elif fun_num == '4':
        if len(person_info) != 0:
            modi_info = input('请输入要修改联系人姓名：')
            for i in person_info:
                if modi_info in i.values():
                    index_num = person_info.index(i)
                    dict_cur_perinfo = person_info[index_num]
                    for title,info in dict_cur_perinfo.items():
                        print(title+':'+info)
                    modi_name = input('请输入新的姓名')
                    modi_phone = input('请输入新的手机号')
                    modi_email = input('请输入新的邮箱')
                    modi_address = input('请输入新的地址')
                    dict_cur_perinfo.update(姓名= modi_name)
                    dict_cur_perinfo.update(手机号=modi_phone)
                    dict_cur_perinfo.update(电子邮箱=modi_email)
                    dict_cur_perinfo.update(联系地址=modi_address)
                    print(person_info)
        else:
            print('通讯录无信息')
    elif fun_num == '5':
        if len(person_info) != 0:
            query_name = input('请输入要查找的联系人姓名：')
            for i in person_info:
                if query_name in i.values():
                    index_num = person_info.index(i)
                    for title,info in person_info[index_num].items():
                        print(title + ':' + info)
                    break
            else:
                print('该联系人不在通讯录中')
        else:
            print('通讯录无信息')
    elif fun_num == '6':
        break







