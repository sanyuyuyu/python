# def primes():
# 	yield 2 
# 	it = _odd_iter
# 	while True:
# 		n = next(it)
# 		yield n 
# 		it = filter(_not_divisible(n),it)


# def is_odd(n):
# 	return n % 2 == 1
# print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))) #删除偶数保留奇数

# def not_empty(s):
# 	return s and s.strip()
# print(list(filter(not_empty,['a','','b'])))  #删除空字符串


# def _odd_iter():
# 	n = 1 
# 	while True:
# 		n = n + 2
# 		yield n 

# def _not_divisible(n):
# 	return lambda x: x % n > 0

# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break



def is_palindrome(n):
	
	if n < 10:
		return True
	re = ""
	cn = n 
	while(cn > 0):
		y = cn % 10
		cn = int(cn/10)
		re += str(y)
	return int(re) == n



