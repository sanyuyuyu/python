# def count():
# 	def f(j):
# 		def g():
# 			return j * j 
# 		return g 
# 	fs = []
# 	for i in range(1,4):
# 		fs.append(f(i))
# 	return fs 
# f1,f2,f3 = count()
# print(count())

# class Solution(object):
# 	def longestCommonPrefix(self,strs):
# 		if not strs: return ""
# 		s1 = min(strs)
# 		s2 = max(strs)
# 		for i,x in enumerate(s1):
# 			if x != s2[i]:
# 				return s2[:i]
# 		return s1


def longestCommonPrefix(self,strs):
	if not strs: return ""
	ss = list(map(set,zip(*strs)))
	res = ""
	for i,x in enumerate(ss):
		x = list(x)
		if len(x) > 1:
			break 
		res = res + x[0]
	return res



