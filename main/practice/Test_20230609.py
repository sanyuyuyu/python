# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return sorted(L,key = lambda x:x[0])
# def by_score(t):
#     return sorted(L,key = lambda x:x[1],reverse= True)

# t = L
# a=by_name(t)
# b=by_score(t)
# print(a)
# print(b)


# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n 
#     return ax

# def laxy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n 
#         return ax 
#     return sum


# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) 
#     return fs

# f1,f2,f3 = count()


def inc():
    x = 0 
    def fn():
        x = x + 1 
        return x 
    return fn

f = inc()





