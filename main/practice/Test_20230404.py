'''
import turtle
turtle.right(199)
turtle.fd(90)
turtle.left(199)
turtle.fd(120)
turtle.right(199)
turtle.fd(120)
turtle.left(199)
turtle.fd(90)
'''
data = input()
num = 0
age = 0
maleNum = 0
while data:
    num += 1
    infoArr = data.split(" ");
    age += int(infoArr[2])
    if infoArr[1] == "男":
        maleNum += 1
    data = input()
age = age / num;
print("平均年龄{:.2f} 男性人数是{}".format(age, maleNum))



















