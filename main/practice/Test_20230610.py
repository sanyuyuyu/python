# class Solution(object):
# 	def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
#         f = lambda x: x.count(min(x))
#         n, ws = len(words), sorted(map(f, words))
#         return [n - bisect.bisect(ws, i) for i in map(f, queries)]

# def now():
# 	print('123')
# f = now
# f()

# def log(func):
# 	def wrapper(*args,**kw):
# 		print('call % s():' % func.__name__)
# 		return func(*args,**kw)
# 	return wrapper


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


