# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-28 16:43:39
import time 

class TimeSpan:
    def __enter__(self):
        self.end = None 
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('耗时:{}毫秒'.format((self.end-self.start)))

if __name__ == '__main__':
    with TimeSpan() as f:
        for i in range(0,1000):
            print(i)



import json 
import traceback
import logging 
logger = logging.getLogger(__name__)

def load_json(file):
    with open(file,'r') as f:
        return json.loads(f.read())
def test():
    try:
        ret = load_json('a.json')
        return {'err': 'success','result': ret}
    except Exception as e：
        logger.error(f"load json exception:{str(e)}")
        logger.error(tracebook.format_exc())
        return {'err': 'exception'}
    ret = load_json('a.json')
    

  
if __name__ == '__main__':
    test()






















