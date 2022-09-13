 




    
import math 
import functools 
def fact(n=1):
        nr = ""
        for i in range(1,n+1):
            nr += "*"+str(i)
        ns = nr.strip("*")
        nss = eval(ns)
        print(f"{ns}={nss}")
        return nss

def fact2(n):
    nr = ''
    for i in range(1,n+1):
        nr += "*"+str(i)
    return eval(nr.strip("*"))

def fact3(n):
    nr = 1
    for i in range(1,n+1):
        nr = nr*i 
    return nr

def fact4(n):
    if n-1 == 0:
        return nr 
    else:
        return fact4(n-1,nr*n)

def fact5(n):
    L = [i for i in range(1,n+1)]
    ret = functools.reduce(lambda x, y:x*y, L)
    return ret

def fact6(n):
    value = math.factorial(n)
    return value 

_initial_missing = object()
def reduce(function, sequence, initial=_initial_missing):
    it = iter(sequence)
    print(type(initial),type(_initial_missing))
    if initial is _initial_missing:
        try: 
            value = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value') from None 
    else:
        value = initial 
    for element in it:
        value = function(value, element)
    return value 
    



 
 




     
       
    












































