'''
def IsPrime(n):
 
    a=int(n/2+1)
 
    j=0
 
    for i in range(2,a):
 
        if n%i==0:
 
            j+=1
 
    if j>0:
 
        print('%d不是素数'%n)
 
    else:
 
        print('%d是素数'%n)
 
n=int(input('请输入一个正整数：'))
 
IsPrime(n)
'''
a = 1.2
b = 2.3
print("变量a=%d,变量b=%d"%(a,b))

c = 'hello'
d = 'exception'
print(c,d,sep='.') #sep修改间隔字符


while True:
	mWorth = input("请依次输入币值和符号(¥/$):")
	if mWorth[-1] in ['$']:
		CNY = (eval (mWorth[0:-1]))*6.8833
		print("可兑换的人民币为%.3f"%CNY)
	elif mWorth[-1] in ['¥']:
		USD = (eval(mWorth[0:-1])) * 0.1452
		print("可兑换的人民币为%.3f"%USD)
	else:
		print("输入有误")