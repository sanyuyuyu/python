file_object = open("test.py",'r') #创建一个文件对象，也是一个可迭代对象
try:
    all_the_text = file_object.read()  #结果为str类型
    print (type(all_the_text))
    print ("all_the_text=",all_the_text)
finally:
    file_object.close()







































