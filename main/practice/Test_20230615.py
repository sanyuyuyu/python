# 1.编写程序，要求程序能根据用户输入的数据计算圆的面积（圆的面积公式：S = πr ^ 2，π取值为3
# .14），并分别输出圆的直径和面积。
# r = int(input('半径：'))
# d = 2 * r
# S = 3.14 * r * r
# print(f'圆的直径是{d}')
# print(f'圆的面积是{S}')

# 2.	已知某煤场有30顿煤，先用一辆载重5顿的汽车运3次，
# 剩下的用一辆载重为1.5顿的汽车运送，请计算还需要运送几次才能送完？编写程序，解答此问题。
# total = 30
# start = 5 * 3
# remain = total - start
# last = int(remain / 1.5)
# print(f'还需要运{last}次')

#3.	编写函数，输出1~100中偶数之和。
# def odd():
#     osum = 0
#     for i in range(1,101):
#         if i % 2 == 0:
#             osum += i
#     print(osum)
# odd()

#4.	已知列表li_one = [1,2,1,2,3,5,4,3,5,7,4,7,8]，编写程序实现删除列表li_one中重复数据的功能。
# li_one = [1, 2, 1, 2, 3, 5, 4, 3, 5, 7, 4, 7, 8]
# last = list(set(li_one))
# print(last)

#5.	已知列表li_num1 = [40, 50, 2, 7]和li_num2 = [30, 60]，
# 请将这两个列表合并为一个列表，并将合并后的列表中的元素按降序排列。
# li_num1 =  [40, 50, 2, 7]
# li_num2 = [30, 60]
# ll = li_num1 + li_num2
# print(f'合并后的结果是{ll}')
#ll.sort()
# ll.reverse()
# print(f"合并之后降序的结果是{ll}")


#6.	编写函数，计算20*19*18*…*3的结果。
# def ride(n):
#     if n == 2:
#         return 1
#     else:
#         return n * ride(n-1)
# print(ride(20))

# li_one = [1,2,1,2,3,5,4,3,5,7,4,7,8]
# new_li =[]
# for i in li_one:
#     if i not in new_li:
#         new_li.append(i)
# print(new_li)
