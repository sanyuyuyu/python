import re
 
 
s = input("请输入一个字符串:").strip()
letters = 0
space = 0
digit = 0
other = 0

for i in s:
    if i.isalpha():  # 判断是否是字母
        letters += 1
    elif i.isspace():  # 判断是否是空白字符
        space += 1
    elif i.isdigit():  # 判断是否是数字
        digit += 1
    else:
        other += 1
 
 
print(f'char = {letters},space = {space},digit = {digit},others = {other}')
 
 
# 2.使用正则表达式
letters = len("".join(re.findall(r"[a-zA-Z]", s)))  # 匹配字母
space = len("".join(re.findall(r"\s+", s)))  # 匹配空白字符
digit = len("".join(re.findall(r"\d+", s)))  # 匹配数字
# 匹配非字母 数字 下划线 此时空白字符也会被匹配到 所以先要将空白字符移除
other_list = re.findall(r"\W", s)
for i in other_list:
    if i.isspace:
        other_list.remove(i)
other = len("".join(other_list))
print(f'char = {letters},space = {space},digit = {digit},others = {other}')