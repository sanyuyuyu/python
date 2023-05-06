#进制转换
# a = int(input('输入要转换的数据：'))
# b = input('输入转换进制：')
# if b == '2':
#     print(f'{bin(a)}')
# elif b == '8':
#     print(f'{oct(a)}')
# elif b == '10':
#     print(f'{int(a)}')
# elif b == '16':
#     print(f'{hex(a)}')

import time
incomplete_sign = 50
print('='*23 + '开始下载'+'='*25)
for i in range(incomplete_sign + 1):
    completed = "*" * 1
    incomplete = '.' * (incomplete_sign - 1)
    percentage = (i / incomplete_sign) * 100
    print('\r{:.0f}%[{}{}]'.format(percentage,completed,incomplete),end='')
    time.sleep(0.5)
print('\n' + '=' * 23 + '下载完成' + '=' * 25)

#商品扫描价格
# one = float(input('第一个扫描的商品价格：'))
# two = float(input('第二个扫描的商品价格：'))
# three = float(input('第三个扫描的商品价格：'))
# total = one + two + three
# print('{:.0f}'.format(total))



import math
fish = math.pow((1.0 + 0.01),3)
net = math.pow((1.0 - 0.01),2)
print(fish * net)
print(fish * net < 1.0 + 0.01)




