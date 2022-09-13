#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-10 21:55:54
# @Last Modified time: 2022-09-13 15:59:30
def get_data_from_file1(path: str) -> str:

  data = ''
    
    with open(path, 'r') as file:
        for line in file.readlines():
            if line == "111.":
                data += line
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


data = ''
    
    with open(path, 'r') as file:
        for line in file.readlines():
            if '111' in line:
                data += line 
                print(data)



