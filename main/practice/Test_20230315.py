'''
one = float(input("扫描的第一个商品价格是:"))
two = folat(input("扫描的第二个商品价格是:"))
total = one + two
print(int(total))'''

'''
import sys
file = sys.stdout  
#向标准输出文件输出
file.write('hello')
'''
#open(file,mode = 'r',buffering = -1)

file = open('text.txt')
file.read(5) #读取5个字符
file.read(2) #继续读取2个字符
file.read()  #再次读取