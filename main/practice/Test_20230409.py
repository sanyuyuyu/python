# class Car():
# 	def __init__(self,make,model,year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.this_year = 2018
# 	def mod_this_year(self,new_year):
# 		self.new_year = new_year
# 	def detection(self):
# 		duration = self.this_year - self.year
# 		price = 30 - 2 * duration
# 		long_time = '你的' + self.make + self.model + '到目前为止已经行驶了' + str(duration)\
# 					+ '年' + '目前价值' + str(price) + '万'
# 		return long_time
# my_car = Car('sansan','aa',2023)
# my_car.mod_this_year(2030)
# my_car.this_year = 2030
# print(my_car.year)
# result = my_car.detection()
# print(result)
# your_car = Car('aa','dd',2022)
# result = my_car.detection()
# print(result)


# def a(x):
# 	return x + 2
# list1 = [2,4,2,3]
# map(a,list1)

# print(map)

a , b = map(int,input().split())
if a > b :
	a , b = b , a
s = 0
for i in range(a,b + 1):
	if i % 2 == 0:
		s += 1
print(S)






