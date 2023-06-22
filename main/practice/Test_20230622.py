# import types
# def fn():
# 	pass

# print(type(fn) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x:x) == types.LambdaType)
# print(type((x for x in range(10))) == types.Generato)

# isinstance(h,Husky)
# isinstance(h,Animal)

# def Mydog(object):
# 	def __len__(self):
# 		return 100

# def readImage(fp):
# 	if hasattr(fp,'read'):
# 		return readData(fp)
# 	return None


# class MyObject(object):
# 	def __init__(self):
# 		self.x = 9
# 	def power(self):

# import types
# def is_func(fn):
# 	return type(fn) == types.FunctionType or type(fn) == types.BulltinFunctionType or type(fn) == types.LambdaTyoe or type(fn) == types.GeneratorType
# print(is_func(abs), is_func(is_func), is_func(lambda x: x**2))


# class Baller(object):

#     def __init__(self, shooting, passing, iq):
#         self.shooting = shooting
#         self.passing = passing
#         self.iq = iq

# curry = Baller(100, 99, 99)
# print(type(curry) == Baller)
# if hasattr(curry, 'shooting'):
#     print('Curry\'s shooting: %s' % getattr(curry, 'shooting'))

# d = {'name':'jam','age':18,'gender':'male'}
# class Object(object):
# 	def __init__(self,note,name):
# 		self.note = note
# 		self.name = name 
# 	def dict2bean(self,dict1):
# 		for k,v in dict1.items():
# 			if hasattr(self,k):
# 				print('has the value')
# 				setattr(self,k,v)
# 				dict1[k] = self.name 

# myobj = Object('name','liu')
# print(myobj.note,myobj.name)
# myobj.dict2bean(d)
# print(d)
# print(myobj.note,myobj.name)


