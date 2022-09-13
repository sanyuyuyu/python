#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-13 16:10:39
# @Last Modified time: 2022-09-13 18:58:19
def test_git_push():
    """测试push提交."""
    ...


# def get_data_from_file(path: str) -> str:
#     """获取path 例如:data.txt文件里的内容"""
#     with open(path, 'r') as fp:
#         data = fp.read()

#     return data


# path = '/Users/wangfeng/wss/python/data.txt'


# data = get_data_from_file(path)
# print(data)


def get_data_from_file1(path: str) -> str:
    """获取path 例如:data.txt文件里的内容"""

    data = ''
    
    with open(path, 'r') as file:
        for line in file.readlines():
            if '111' in line:
                data += line 
                print(data)

    return data       
          
   
   
                
            # print(line.strip())



        # line = fp.readline()
        # while line:
        #     line = fp.readline()
        #     if not line:
        #         break
        #     data += line

    



print(data)









