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