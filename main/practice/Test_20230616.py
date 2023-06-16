# li_one = [1,2,1,2,3,5,4,3,5,7,4,7,8]
# new_li =[]
# for i in li_one:
#     if i not in new_li:
#         new_li.append(i)
# print(new_li)


# def guess(number):
#     i = 0
#     original_number = number
#     while number != 1:
#         if number % 2 == 0:
#             number = number / 2
#         else:
#             number = number * 3 + 1
#         i += 1
#     print(f"{original_number}经过{i}次变换后回到1")
#
# num = int(input('请输入一个大于1的正整数：'))
# guess(num)




# std1 = { 'name': 'Michael', 'score': 98 }
# std2 = { 'name': 'Bob', 'score': 81 }

# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))


# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))