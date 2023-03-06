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