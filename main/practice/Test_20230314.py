with open('9981.txt','w') as f:
 
    for i in range(1,10):
 
        for j in range(1,i+1):
 
            a=str(j)+'*'+str(i)+'='+str(i*j)+'\t'
 
            print(a,end='')
 
            f.write(a)
 
        print()
 
        f.write('\n')

        with open('9981.txt','w') as f:
 
    for i in range(1,10):
 
        for j in range(1,i+1):
 
            a=str(j)+'*'+str(i)+'='+str(i*j)+'\t'
 
            print(a,end='')
 
            f.write(a)
 
        print()
 
        f.write('\n')