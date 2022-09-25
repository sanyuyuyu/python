# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-25 22:00:07


def test():
    books = ('骆驼祥子', '海底两万里', '假如给我三天光明', '朝花夕拾')
 
    reading = (book for book in books if len(book) <= 4)
 
    print("long书")
    for book in reading:
        print(" ->《{}》".format(book))
 
    print("long字")
 
 
if __name__ == '__main__':
    test()
 
def test():
