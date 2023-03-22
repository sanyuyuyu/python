'''
score = int(input('请输入一个整数:'))
if score < 0 or score > 100:
    print('程序出错')
elif score > 90:
    print("成绩是优秀")
elif score >=60:
    print("成绩是合格")
elif score <60:
    print("成绩不合格")
else:
    print("没有成绩哦")
'''
'''
a = float(input("输入一个a:"))
b = float(input("输入一个b:"))
c = input("输入的运算符:")
if c == '+':
    print(a+b)
if c == '*':
    print(a*b)
if c == '-':
    print(a-b)
if c == '/':
    if b != 0:
        print(a/b)
    else:
        print("第二个数字不能为0")
else:
    print("这个运算符还带待开发")
'''
'''
d = int(input("请输入一个整数："))
for d in range(10):
    if d >= 1:
        print("很遗憾，你猜小了。")
    elif d > 10:
        print("很遗憾，你猜大了。")
    elif d == 5:
        print("恭喜，猜数成功。")
'''
'''
Guess_num = int(input("请输入要猜的数据:"))
for i in range(1,6):
    number = input("请输入第"+str(i)+"次猜测的数字：")
    if number.isdigit() is False:
      print("请输入一个正确的数字")
    elif int(number) < 0 or int(number) > 100:
        print('请输入一个正确的数字')
    elif int(number) == int(Guess_num):
        print("恭喜你，使用%d猜对了"%i)
        break
    elif int(number) < int(Guess_num):
        print("很遗憾，猜小了。")
    elif int(number) > int(Guess_num):
        print("很遗憾，猜大了。")
    if i == 5:
        print("您使用%d次机会猜数字，游戏结束，设定数字为%d" % (i, Guess_num))
'''
'''
i = int(input("1-100的数："))
while i in range(1,101):
    if i % 2 == 0:
        print("输出的是偶数")
        break
    else:
        print("输出的是奇数")
        break
'''
'''
a = int(input("请输出一个数："))

if a > 0:
    print("输出的是正数")
elif a < 0:
    print("输出的是负数")
else:
    print("0")
'''

'''
for i in range(2,101):
    flag = True
    for j in range(2,i):
        if i % j == True :
            flag = False
            break
    if flag:
        print(i)
'''
'''
i = 2
while(i < 101):
    cnt = 0
    for n in range(2,101):
        if i % n == 0:
            cnt += 1
            continue
    if cnt == 1:
        print(i)
    i += 1
'''
'''
for i in range(2,100):
    aa = True
    for j in range(2,i):
        if i % j == 0:
            aa = False
    if aa == True:
        print(i)
'''


for i in range(1,11):
    print('-')
    for j in range(1,i):
        print("---",end='')

