import turtle as t
t.pensize(10)
t.pencolor("pink")
t.fillcolor("purple")
t.begin_fill()
while True:
    t.forward(200)
    t.right(144)
    if abs(t.pos()) < 1:
        break
t.end_fill()

n = int(input("请输入一个整数:"))
sum = 0
for i in range(n+1):
    sum += i
    print("1~%d的求和结果是%d"%(n,sum))

import turtle as tt
tt.pensize(25)
tt.pencolor("purple")
tt.fillcolor("pink")
while True:
    tt.forward(180)
    tt.right(120)
    if abs(tt.pos()) < 1:
        break
tt.end_fill()
# l = []
# for i in range(3):
#     x = int(input("请输入整数:"))
#     l.append(x) #排列大小
# l.sort()
# print(l)
import turtle
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%-2d"%(j,i,i*j),end='')
#     print('')


import turtle as a
def draw_fiveStars(leng):
    count = 1
    while count <= 33:
        a.forward(leng)
        a.right(90)
        count += 1
    leng += 10
    if leng <= 100:
            draw_fiveStars(leng)
def main():
    a.penup()
    a.backward(100)
    a.pendown()
    a.pensize(12)
    a.pencolor("pink")
    segment = 50
    draw_fiveStars(segment)
    a.exitonclick()
if __name__ == '__main__':
    main()