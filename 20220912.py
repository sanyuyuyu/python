# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-12 20:28:32
# @Last Modified by:   sanyuyuyu
# @Last Modified time: 2022-09-12 22:32:23


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
            # print(line.strip())
            data += line

        # line = fp.readline()
        # while line:
        #     line = fp.readline()
        #     if not line:
        #         break
        #     data += line

    return data


data = get_data_from_file1('data.txt')
print(data)


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

