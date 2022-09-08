#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-06 19:42:23
# @Last Modified time: 2022-09-08 21:10:48
from datetime import datetime, timedelta
if __name__ == '__main__':
    today = datetime.now()
    print(today)
    print(today.strftime("%d/%m/%y"))
    print(today.strftime("%A %d %B %Y"))
from datetime import *
now = datetime.now()
y = now + timedelta(days=-1)
m = now + timedelta(days=1)


from datetime import datetime 
from time import time, mktime 

class TimeSpan:
    def __init__(self) -> None:
        self.start = round(time() * 1000)
 

    def elapse_mill_secs(self):
        end = round(time() * 1000)
        return end-self.start

    def elapse_secs(self):
        return (self.elapse_mill_secs())/1000

if __name__ == '__main__':
    s = TimeSpan()

    for i in range(0, 100000):
        pass
    print('耗时： {} 毫秒'.format(s.elapse_mill_secs()))
    print('耗时： {} 秒'.format(s.elapse_secs()))


from datetime import date, timedelta
from calendar import monthrange
 
def next_month(d):
    offset = monthrange(d.year, d.month)
    first_weeky_day, day_in_month = offset 
    value = d+timedelta(days_in_month)
    return value
 
def for_each_month(start, finish, action):
    while start < finish:
        action(start)
        start = next_month(start)
 
if __name__ == '__main__':
    for_each_month(
        date(2008, 1, 1),
        date.today(),
        lambda d: print(d)





















