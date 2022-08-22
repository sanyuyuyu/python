#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-07 17:57:35
# @Last Modified time: 2022-08-22 21:31:12


file_object = open("test.txt",'r') #创建一个文件对象，也是一个可迭代对象
try:
    all_the_text = file_object.read()  #结果为str类型
    print (type(all_the_text))
    print ("all_the_text=",all_the_text)
finally:
    file_object.close()


file_object = open("test.txt")
line = file_object.readline()
while line:
    print(line, end = '')
    line = file_object.readline()
file_object.close()

f = open("test.txt",'r')               # 返回一个文件对象  
line = f.readline()               # 调用文件的 readline()方法  
while line:  
    print (line)                   # 后面跟 ',' 将忽略换行符  
    #print(line, end = '')       # 在 Python 3 中使用  
    line = f.readline()   
f.close()



content = "lisa,mike,"
open("test.txt",'w').write(content)


with open("/Users/alpha/wss/python/test.txt","a") as file:
    file.write("lisi,")

file_object = open("test.txt","a+")
content = file_object.read()
print(content)
file_object.close()






content = 'test.txt'

with open(content,'w') as file_object:
    file_object.write("111.\n")
    file_object.write("222.\n")



line1 = "333."
line2 = "444."
line3 = "555."


with open("test.txt",'a') as out:
    out.write('{}\n{}\n{}\n'.format(line1,line2,line3))




import pandas
import numpy as np 
#将test.txt文件中的内容写入data.txt文件
with open('data.txt','ab') as f:
    f.write(open('test.txt','rb').read())


#读取文件
with open("./test.txt") as file_object:
    content = file_object.read() #file_object.read() 用于读取文件内容，以str形式储存在变量content里
    print(content)

#逐行读取
file_name = "test.txt"

with open(file_name) as file_object:
    for line in file_object:
        print(line)       # 此时行与行之间会有空行，因为打印了换行符
        print(line.rstrip())    # 此时没有空行























































