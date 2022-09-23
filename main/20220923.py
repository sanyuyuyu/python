# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-23 21:46:50
# -*- coding: UTF-8 -*-

#统计偶数个数
if __name__ == '__main__':
    pi = [2,3,4,5,56,2]
    even_count = 0
    for i in pi:
        even_count += 1 if i % 2 == 0 else 0 
    assert even_count == 4



if __name__ == '__main__':
    pi = [3, 14, 15, 9, 26, 5, 35, 8, 97, 932]
    even_count = 0
 
    for i in pi:
        even_count += 2 if i % 4 == 0 else 1 if i % 2 == 0 else 0
    assert even_count == 6

