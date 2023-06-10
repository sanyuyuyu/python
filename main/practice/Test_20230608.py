# def add(x,y,f):
#     return f(x)*f(y)
# print(add(5,-6,abs))

from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


def primes():
    yield 2
    it = _odd_iter() 
    while True:
        n = next(it) 
        yield n
        it = filter(_not_divisible(n), it)


def f(n):
    p=''
    n=str(n)
    x=len(n)-1
    y=[]
    while x>=0:
        y.append(n[x])
        x-=1
    for result in y:
        p+=result
    return p
def is_palindrome(n):
    return str(n)==f(n)

    
