# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-12 20:28:32
# @Last Modified by:   sanyuyuyu
<<<<<<< HEAD
# @Last Modified time: 2022-09-13 17:29:25
=======
# @Last Modified time: 2022-09-12 22:32:23
>>>>>>> b42006ea7d5c4d11d9d81cc937ddca73cee14569


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


<<<<<<< HEAD




=======
a = ['a','b','c']


def get_abc(a):
    ...
    # 定义一个字符串
    data = ''
    # 遍历传进来的数组
    for _ in a:
        # 字符串相加
        data += _
    # 返回最终的数据
    return data


def get_abc1(a):
    return ''.join(a)


print(get_abc(a))
print(get_abc1(a))
>>>>>>> b42006ea7d5c4d11d9d81cc937ddca73cee14569

