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
 
for n in range(100,201):
 
    IsPrime(n)

for chicken in range(0,36):

    if chicken*2 + (35-chicken)*4 ==94:
        
        print("chicken%d"%chicken,"rabait%d"%(35-chicken))

import random
 
chars="abcdefghijklmnopqrstuvwxyz"
 
a=[random.choice(chars) for j in range(10)]
 
a=''.join(a) #将列表中所有字符连接成字符串
 
print(a)
 
b=input('请输入上文内容：')
 
num=0
 
i=1
 
while i:
 
    if len(a)!=len(b):
 
        print('输入长度不相等')
 
        i=1
 
    else:
 
        i=0
 
for a_ch,b_ch in zip(a,b):
 
    if a_ch==b_ch:
 
        num+=1
 
rate=num/len(a)
 
print('准确率为：',rate)