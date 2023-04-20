# rank , name , number = input().split()
# number = int(number)
# decount = 0
# if rank == '普通会员':
# 	decount = 0.95
# elif rank == '银会员':
# 	decount = 0.9
# elif rank == '金会员':
# 	decount = 0.85
# else:
# 	decount = 1

# price = 0
# if name == '商品一':
# 	price = 100
# elif name == '商品二':
# 	price = 200
# elif name == '商品三':
# 	price = 300
# last_price = int(decount * price * number)
# print(last_price)


# n = int(input())

# if n > 10:
# 	print(2 * n)
# elif n > 20:
# 	print(3 * n)
# else:
# 	print(0)


# n = int(input())

# if n < 10:
# 	print(10 * n)
# elif n >= 10:
# 	print(9 * n)




# n = int(input())

# for i in range(30):
# 	if str(n) == str(n)[::-1]:
# 		print(i)
# 		break
# 	else:
# 		n = n + int(str(n)[::-1])
	
# else:
# 	print(30)


import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='test')
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT * from students;")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()

