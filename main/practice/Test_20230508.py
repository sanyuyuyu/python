# # print('%d,%s'%(6,'s'))
# # print('{}'.format(11))
# a = int(input('请输入要转换的数据：'))
# b = int(input('请输入要转换的进制：'))
# if b == 2:
#     print(f'{bin(a)}')
# elif b == 8:
#     print(f'{oct(a)}')
# elif b == 16:
#     print(f'{hex(a)}')
# elif b == 10:
#     print(f'{int(a)}')


#
# a = 'abcdefghaijklmnoapqrst'
# print(a.find('a'))
# print(a.rfind('a'))
# print(a.index('a'))
# print(a.rindex('a'))
# print(a.replace('a','s'))
#

#
# a = '  i like eat cholocate  '
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())
# print(a.split('a'))
# print(a.rsplit('a'))
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
#

#
# senstive_character = '牛肝菌'
# test_senstive = input('请输入一段话：')
# for line in senstive_character:
#     if line in test_senstive:
#         test_senstive = test_senstive.replace(line,'*')
# print(test_senstive)
#
# string = input('请输入一段话：')
# print('1.删除空格')
# print('2.英文标点替换')
# print('3.首字母大写')
# print('4.退出')
#
#
# while True:
#     option = int(input('请输入功能选项：'))
#     if option == 1:
#         string = string.replace('','')
#     elif option == 2:
#         for i in string:
#             if i == ',':
#                 string = string.replace(',','，')
#             elif i == '.':
#                 string = string.replace('.','。')
#             elif i == '?':
#                 string = string.replace('?','？')
#             elif i == ':':
#                 string = string.replace(':','：')
#         string = string
#         print(string)
#     elif option == 3:
#         string = string.upper()
#         print(string)
#     elif option == 4:
#         break

# s = 'AbcDeFGhIJ'
# count = 0
# for i in s:
#     for j in s.lower():
#         if i == j:
#             count += 1
# print(count)

# string = 'Life is short.I use python'
# a = string.split()
# for i in a:
#     if i == 'python':
#         print(a)
string = 'Life is short.I use python'
if string.find('python'):
    string = string.replace('python','Python')
    print(string)
else:
    print(string)













































