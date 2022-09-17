# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-12 20:28:32
# @Last Modified by:   sanyuyuyu
# @Last Modified time: 2022-09-13 19:53:52


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
           if int(line.replace(".","")) % 2 == 0:
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

    


data = get_data_from_file1('data.txt')
print(data)


def get_data_from_file1(path: str) -> str:
    """获取path 例如:data.txt文件里的内容"""


    data = ''
    
    with open(path, 'r') as file:      
        for line in file.readlines():
            #输出111.
           if '111.\n' in line:
            data += line 
            print(data)

    return data       
          

data = get_data_from_file1("data.txt")




def get_data_from_file1(path: str) -> str:
    data = ''
    with open(path, 'r') as file:      
        for line in file.readlines():
            #输出111.
           if line == '111.':
            data += line 
            print(data)

    return data  

data = get_data_from_file1("data.txt")









