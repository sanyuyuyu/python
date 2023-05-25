# def f(x):
# 	return x * x
# r = map(f,[1,2,3,4,5])
# print(list(r))


# from functools import reduce
# def add(x,y):
# 	return x + y 
# print(reduce(add,[1,23,4]))

# from functools import reduce 
# def fn(x,y):
# 	return x * 10 + y 
# print(reduce(fn,[1,3,5,7,9]))

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))