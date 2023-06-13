# import sys

# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')

# if __name__=='__main__':
#     test()


# def _private_1(name):
#     return 'Hello, %s' % name

# def _private_2(name):
#     return 'Hi, %s' % name

# def greeting(name):
#     if len(name) > 3:
#         return _private_1(name)
#     else:
#         return _private_2(name)


import sys

def test():
    args = sys.argv
    if 1 == len(args):
        print('hello world!')
    elif 2 == len(args):
        print(f'hello {args[1]}')
    else:
        print('args too many')

if __name__ =='__main__': 
 
    test()

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting_2(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)



