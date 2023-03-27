'''
k = 0
while True:
    s = input('请输入q退出：')
    if s == 'q':
        k += 1
        continue
    else:
        k += 2
        break
print(k)
'''

s = 0
def fun(num):  #s  在函数内无定义。。。。。
    try:
        s += num
        return s
    except:
        return 0
    return 5
print(fun(2))