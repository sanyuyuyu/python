# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-24 21:40:42


if __name__ == '__main__':
    list = [24,556,332,442,24,24]
    print('')
    print('偶数')
    even = [n for n in list if n % 2 == 0]

    for n in even:
        print(n)
    print('')



if __name__ == '__main__':
    obj_list = [
        {"key": "day1", "value": "大雨", 'tags': ["不热"]},
        {"key": "day2", "value": "很热很热", 'tags': ["热"]},
        {"key": "day3", "value": "热热", 'tags': ["不热"]}
    ]
 
    print('')
    print("# 过滤出不热的日子")
 
    non_hot_days = [d for d in obj_list if '不热' in d['tags']]
 
    for day in non_hot_days:
        print("* [{}]: {}".format(day['key'], day['value']))
 
    print('')
 
