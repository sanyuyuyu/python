'''问题1(5分): 对“命运.txt"文件进行字符频次统计,输出频次最高的中文字符(不包含标点符号)
及其频次,字符与频次之间采用英文冒
号”:"分隔,示例格式如下:'''

file = open("命运.txt", "r", encoding="utf-8")
info = file.read()
d = {}
for s in info:
    if s not in "，。？《》！【】“”‘’、":
        d[s] = d.get(s, 0 ) + 1
arr = list(d.items())
arr.sort(key=lambda item:item[1], reverse=True)
file.close()
print("{}:{}".format(arr[0][0],arr[0][1]))


file = open("命运.txt", "r", encoding="utf-8")
info = file.read()
d = {}
for s in info:
    if s not in "\n":
        d[s] = d.get(s, 0) + 1
file.close()
ls = list(d.items())
ls.sort(key=lambda item:item[1], reverse=True)
for i in range(10):
    print("{}".format(ls[i][0]), end="")










