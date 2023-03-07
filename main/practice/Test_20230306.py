sum = 0
for i in range(1,101):
	sum += i
	print("1~100和",sum)

sum = 0
for ii in range(5,101,5):
	sum += i
	print("5+15+20+...+100 = ",sum)


a=int(input("请输入第一个正整数："))
b=int(input("请输入第一个正整数：")) 
while(a):
    if a<b: 
        t=a
        a=b
        b=t
        a%=b
 
print("这两个正整数的最大公约数为：",b)

#提取出生日日期
m=input('请输入一个18位的身份证号：')
if len(m)<18: 
    print("输入错误！")
else: 
    a=int(m[6:10]) 
    b=int(m[10:12])
    c=int(m[12:14])
    print('出生日期是%d年%d月%d日'%(a,b,c))


i=1
while i:
    m=float(input('请输入一个月份：'))
    if m>12 or m<=0 or m%1!=0:
        i=1
        print('输入的数据为非法数据，请重新输入！')
    else:
        i=0
if m>0 and m<=3:
    print('%d月所属第一季度'%m)
elif m>=4 and m<=6:
    print('%d月所属第二季度'%m)
elif m>=7 and m<=9:
    print('%d月所属第三季度'%m)
elif m>=10 and m<=12:
    print('%d月所属第四季度'%m)











