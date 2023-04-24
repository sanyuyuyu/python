# def test(x):
# 	return x * x


# lambda x, y: x + y


# # print(list(map(test, [1,3,5,8])))
# print(list(map(lambda x : x * x, [1,3,5,8])))


# s = [1,2,3,4,5,6]
# s.append(7)
# s.remove(3)
# s[2] = 10
# print(s)
# # s[3]

# print((2*i*1 for i in range(10)))


# d = {'name': 1,'age': 23}

# # add
# d['male'] = 'female'
# print(d)
# del(d['name'])
# d.items()
# # delete
# a = 'name' in d
# print(a)


# for k, v in d.items():
# 	print(k, v)


# for k in d.keys():
# 	print(k)

# for v in d.values():
# 	print(v)


# lst = [1,2,3,9,5]
# #lst.reverse()
# lst1 = list(reversed(lst)) # 反转
# lst.append(4) # 追加
# lst.remove(2) # 删除
# lst.insert(0,1) # 插入
# lst.sort() # 排序
# lst2 = list(sorted(lst))
# print(lst)
# print(lst1)
# print(lst2)


d = {'zs':2,'ls':3}
d['age'] = 18 # 增加一个键值对
dd = d.copy() # 复制
del(d['zs']) # 删除
print(list(d.keys())) # 输出键值名
print(list(d.values())) # 输出键值
print(d.pop('ls')) # 随机弹出一个键值对x
print(d)
print(dd)


