a = set() #集合 不重复
print(a,type(a))
b = {} #元组
print(b,type(b))
c = ['liyuan','zhangsan','lisi'] #列表
print(c,type(c))
d = {'1','2','3'}
d.add('4') #增加4
d.remove('2') #移除2
#d.clear()
e = len(d)
print(d)
print(e)
print(c[1]) #索引输出第一个列表内容
print(c[1:3]) #输出第一个到第三个列表内容

ls = ['s','a']
ls.append('a')
ls.insert(1,'c')
ls.pop(2)
ls.remove('c')
ls.reverse()
g = ls.copy()
print(ls)
print(g)
