
a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a / b
    a,b = a + b,a
print (s)



def draw(num):

    a="*"*(2*(4-num)+1)

    print(a.center(9,' '))

    if num!=1:

        draw(num-1)

        print(a.center(9,' '))
        aa
draw(4)




def _odd_iter():

    n = 1

    while True:

        n = n + 2

        yield n




def primes():

    yield 2

    it = _odd_iter() # 初始序列

    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列




def is_palindrome(n):

    L = [i for i in str(n)]

    return L == L[::-1]

# 测试:

output = filter(is_palindrome, range(1, 1000))

print('1~1000:', list(output))

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:

    print('测试成功!')

else:

    print('测试失败!')

#统计英文字母、空格、数字和其它字符的个数

string=input("输入字符串：")

alp=0
num=0
spa=0
oth=0

for i in range(len(string)):

    if string[i].isspace():

        spa+=1

    elif string[i].isdigit():

        num+=1

    elif string[i].isalpha():

        alp+=1

    else:

        oth+=1

print('space: ',spa)
print('digit: ',num)
print('alpha: ',alp)
print('other: ',oth)






##匿名函数 lambda

lambda x:x*x

# 就等价于

def f(x):

    return x*x

# 匿名函数可以赋值给一个变量。

f = lambda x: x+x

print(f(1))

#也可以作为函数返回值

def func():

    return lambda x : x+x

print(func()(2))

#practice

l = list(filter(lambda x : x % 2,range(1,20))) #filter 筛选出符合条件的

print(l)



L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

high = 200
total = 100

for i in range(10):

    high/=2

    total+=high

    print(high/2)

print('总长', tatal)






























