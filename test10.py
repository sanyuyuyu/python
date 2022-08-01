#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-07-31 15:01:28
# @Last Modified time: 2022-08-01 19:08:30

list(reversed(2,3,5,1,6))
[6,1,5,3,2]


x = [1,1,0]
y = [1,1,9]
all(x)
F
all(y)
T


seaons = ['spring','summer','autumn','winter']
list(enumerate(seaons))
[(0,'spring'),(1,'summer'),(2,'autumn'),(3,'winter')]
list(enumerate(seasons,10))
[(10,'spring'),(11,'summer'),(12,'autumn'),(13,'winter')]


x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y)
list(zipped)
[(1,4),(2,5),(3,6)]
z = [7,8,9]
list(zipped)
[(1,4,7),(2,5,8),(3,6,9)]


z = 'fish'
zipped = zip(x,y,z)
list(zipped)
[(1,4,'f'),(2,5,'i'),(3,6,'s')]
import itertools
zipped = itertools.zip_longest(x,y,z) 
list zipped
[(1,4,'f'),(2,5,'i'),(3,6,'s'),(none,none,'h')]


mapped = map('fish' )
list(mapped)
[70,105,115,104] 


mapped = map(pow,[2,3,10],[5,2,3])
list(mapped)


list(filter(str,islower,'fish')























































































