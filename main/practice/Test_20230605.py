# import math 
# print(math.sqrt(1024))

# wf = open('test.txt','w',encoding = 'utf-8')
# wf.write('Tom')
# wf.writelines(['hello\n','python'])
# wf.close()

# with open('test.txt','w',encoding='utf-8') as wf:
# 	wf.write('Tom\n')
# 	wf.writelines(['hello\n','Python'])

# with open('test.txt', 'r', encoding='utf-8') as rf:
#     print('readline-->', rf.readline())
#     print('read-->', rf.read(6))
#     print('readlines-->', rf.readlines())


with open('test.txt','rb+') as f:
	f.write(b'123456789')
	#文件对象位置
	print(f.tell())
	#移动到文件的第四个字节
	f.seek(3)
	print(f.read(1))
	print(f.tell())
	f.seek(-2,2)
	print(f.tell())
	print(f.read(1))





