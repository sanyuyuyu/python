#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-05 21:21:30
# @Last Modified time: 2022-09-05 22:05:50


#获取当前日期
from datetime import datetime
now = datetime.now()
#获取今天
datetime.today()
#获取指定日期
datetime.date(y,m,d)
datetime.time(h,m,s)
datetime(y,m,d,h)
#输出指定格式
print('strftime():', now.strftime("%Y-%m-%d"))




from datetime import *
now = datetime.now()
y = now + timedelta(days=-1) #明天
m = now.timedelta(days=1) #明天

import datetime  
year,month,day= 2022,9,5 
weekday = ['周一','周二','周三','周四','周五','周六','周日']
i = datetime.date(year,month,day).weekday()
print(weekday[i]

i = datetime.date(year,month,day).isweekday()
print(weekday[i-1])


wday = datetime.date(year,month,day).strftime('%a')
print(wday)





































