a=['学号：1907381106',
 
   '姓名：zhangsan'
 
   ]
 
f=open("学号姓名.txt",'w',encoding='utf8')
 
f.writelines(a)
 
f.close()
 
print('写入成功!')

f1=open("text1.py","r",encoding='utf8')
 
f2=open("text2.py","w",encoding='utf8')
 
lines=f1.readlines()
 
for i in lines:
 
    if len(i)!=1 and not(i.startswith("#")):
 
        f2.writelines(i)
 
f1.close()
 
f2.close()
 
print('成功！')