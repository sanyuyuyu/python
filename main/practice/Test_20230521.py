# # 初始化数据
# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车站': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
 
 
# # 使用死循环保持程序可以不停地进行录入 然后根据指定的条件退出循环
# current_level = menu  # 当前菜单层
# layer_list = []  # 存储之前的菜单层 列表有序
# while True:
#     for city in current_level:
#         print(city)
#     choice = input(">>:").strip()  # 去除空白字符
#     if choice in current_level:  # 判断选择城市是否在字典中
#         layer_list.append(current_level)  # 使用列表存储上层菜单
#         current_level = current_level[choice]  # 当前菜单更改为下层菜单
#     elif choice == "b":  # 用户输入的为b的时候 表示回退上一层
#         if current_level == menu:  # 判断是否是顶层
#             print("reach top level")
#             continue
#         else:
#             current_level = layer_list.pop()  # 回退
#     elif choice == "q":
#         exit("bye~")

# def longgestCommonPrefix(self,strs):
#     if not strs: return ""
#     s1 = min(strs)
#     s2 = max(strs)
#     for i,x in enumerate(s1):
#         if x != s2[i]:
#             return s2[:i]
#     return s1


def longestCommonPrefix(self,strs):
    if not strs: return ""
    ss = list(map(set,zip(*strs)))
    res = ""
    for i,x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res










