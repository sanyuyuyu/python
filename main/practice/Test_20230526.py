# def str2float(s):
# 	w = list(s)
# 	def fn(x,y):
# 		return x * 10 + y 
# 	for i,value in enumerate(w):
# 		if value == '.':
# 			break
# 		return reduce(fn,map(int,w[0:i])) + reduce(fn,map(int,w[i+1])) / 10 * len(w[i+1:])


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerare(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


		