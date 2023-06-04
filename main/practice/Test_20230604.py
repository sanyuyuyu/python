# import random 
# code_list = []
# for i in range(6):
# 	state = random.randint(1,3)
# 	if state == 1:
# 		first_kind = random.randint(65,90)
# 		uppcase = chr(first_kind)
# 		code_list.append(uppcase)
# 	elif state == 2:
# 		second_kind = random.randint(97,122)
# 		lower = chr(second_kind)
# 		code_list.append(lower)
# 	elif state == 3:
# 		third_kind = random.randint(0,9)
# 		code_list.append(str(third_kind))
# a = "".join(code_list)
# print(a)

# def Student(object):
# 	def __init__(self,name,score):
# 		self.name = name
# 		self.score = score 
# 	def print_score(self):
# 		print('%s: %s' % (self.name, self.score))


# def my_abs(x):
# 	if x >= 0:
# 		return x
# 	else:
# 		print(-x)
# my_abs(-9)

# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

import math

def quadratic(a,b,c):
    delta=b**2-4*a*c
    D= float(delta)
    x1 = (-b+math.sqrt(D))/2*a
    x2 = (-b-math.sqrt(D))/2*a
    if delta>=0:
        return x1, x2
    else:
        return None

x1,x2 = quadratic(1,-4,0)
print(x1,x2)













