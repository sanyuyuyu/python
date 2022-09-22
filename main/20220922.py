# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-22 21:55:15



import numpy as np 

def get_top_n(arary, top_n):
    top_n_indexs = np.argsort(array)[:-(top_n+1):-1]
    results = [arrary[index] for index in top_n_index]
    return results 
if __name__ == '__main__':
    ret = get_top_n(np.arrary([1,3,34,2,]), 3)
    print(ret)
