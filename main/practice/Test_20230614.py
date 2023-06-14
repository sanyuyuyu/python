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

#
# def all_goods():
#     goods = {'可口可乐': 2.5, '百事可乐': 2.5, '冰红茶': 3, '脉动': 3.5, '果缤纷': 3, '绿茶': 3, '茉莉花茶': 3, '尖叫': 2.5}
#     return goods
# def show_goods():
#     for x, y in all_goods().items():
#         print(x, ':', str(y) + '元')
# def total(goods_dict):
#     count = 0
#     for name, num in goods_dict.items():
#         total_money = all_goods()[name] * num
#         count += total_money
#     print('需要支付金额：', count, '元')
# def main():
#     goods_dict = {}
#     print('饮 品 自 动 售 货 机')
#     show_goods()
#     print('输入q完成购买')
#     while True:
#         goods_name = input('请输入购物的商品：')
#         if goods_name == 'q':
#             break
#         if goods_name in [g_name for g_name in all_goods().keys()]:
#             goods_num = input('请输入购物数量:')
#             if goods_num.isdigit():
#                 goods_dict[goods_name] = float(goods_num)
#             else:
#                 print('商品数量不合法')
#         else:
#             print('请输入正确的商品名称')
#     total(goods_dict)
#
# if __name__ == '__main__':
#     main()


# def same():
#     for i in range(1,1000):
#         a = int(i / 100)
#         b = int((i % 100)/10)
#         c = int(i % 10)
#         if i == (a ** 3 + b ** 3 + c ** 3):
#             print('{}水仙花数'.format(i))
# same()


# def total(c):
#     for i in range(1,101):
#         c += 1
#     print(c)
# total(0)


# def fsum(n):
#     c = 0
#     for i in range(1, n+1):
#         c += i
#     print(c)
# fsum(100)

#
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return fact(n-1) * n
# print(fact(10))
#
# def merge_sort(li):
#     n = len(li)
#     if n == 1:
#         return li
#     mid = n // 2
#     left = li[:mid]
#     right = li[mid:]
#
#     left_res = merge_sort(left)
#     right_res = merger_sort(right)
#     result = merge(left_res,right_res)
#     return result
#
# def merge(left,right):
#     result = []
#     left_index = 0
#     right_index = 0
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             result.append()




