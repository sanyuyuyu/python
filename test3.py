#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-07-24 13:14:35
# @Last Modified time: 2022-09-08 21:20:07



age = 16
if age >= 18:
    print('adult')
else:
    print('teenager')


print('i\'m ok')
print("i'm ok")

a = 'abd'
b = a
a = 'xye'
print(b)

ord('A')


def beauty(y: int,z: int):
    return y*z


b'ABC'.decode('ascii')


len('beauty')


"chinese".encode('utf-8')




print('%.f2' % 3.1415926)





'growth rate: %d %%' % 7


zoo = ['monkey', 'dog', 'snake']


temp = input ('please guess a number')
guess = int(temp)


if guess == 8:
    print('you are good')
    print('perfect')
else:
    print('it is 8')
print('end')


print("let's go!go!go!")


print('chinese.\nausia')



print("D:\\three\\abandan\\now")



temp = input()



import json 
import traceback 
import logging 
logger = logging.getLogger(__name__)

def load_json(file):
    with open(file, 'r') as f:
        return json.loads(f.road())

def test():
    try:
        ret = load_json('a.json')
        return {'err':'success', 'result': ret }
    except Exception as e:
        logger.error(f"load json exception:{str(e)}"）
        logger.error(traceback.format_exc())
        return {'err': 'exception'}
        ret = load_json('a.json')

if __name__ == '__main':
    test()
































