# import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('begin call')
#         result = func(*args, **kwargs)
#         print('end call')
#         return result
#     return wrapper


# import functools
# def log(func):
#     def wrapper(*args,**kwargs):
#         print('begin call')
#         result = func(*args,**kwargs)
#         print('end call')
#         return result 
#     return wrapper

# def my_function():
#     for i in range(101):
#         print(i**3)
# my_function()


# def log(text=""):
#     if isinstance(text,str):
#         def d(func):
#             import functools
#             def w(*args,**kw):
#                    print(f'text:{text},func.__name__:{func.__name__},begin call')
#                 result = func(*args,**kw)
#                 print(f'text:{text},func.__name__:{func.__name__},end call')
#                 return result
#             return w
#         return d
#  import functools
#     def w(*args,**kw):
#         print(f'func.__name__:{text.__name__},begin call')
#         result = text(*args,**kw)
#         print(f'func.__name__:{text.__name__},end call')
#         return result
#     return w
















