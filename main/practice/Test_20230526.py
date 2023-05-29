# def str2float(s):
# 	w = list(s)
# 	def fn(x,y):
# 		return x * 10 + y 
# 	for i,value in enumerate(w):
# 		if value == '.':
# 			break
# 		return reduce(fn,map(int,w[0:i])) + reduce(fn,map(int,w[i+1])) / 10 * len(w[i+1:])


# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         if not strs: return ''
#         s1 = min(strs)
#         s2 = max(strs)
#         for i,x in enumerare(s1):
#             if x != s2[i]:
#                 return s2[:i]
#         return s1



def calc_sum(*args):
	ax = 0 
	for n in args:
		ax = ax + n 
	return ax


def laxy_sum(*args):
	def sum():
		ax = 0 
		for n in args:
			ax = ax + n 
		return ax 
	return sum



def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i 
		fs.append(f)
	return fs 
f1,f2,f3 = count()










