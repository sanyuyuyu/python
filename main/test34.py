#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-08 13:42:17
# @Last Modified time: 2022-09-10 21:51:52
import os 
 

def ordered_list_dir(dir):
    entries = os.listdir(dir)
    entries.sort()
    return entries


if __name__ == '__main__':
    entries = ordered_list_dir('./')
    for entry in entries:
        print(entry)


import os 

def retrieve_file_paths(dir_name):
    file_paths = []
    abs_dir_name = os.path.abspath(dir_name)
    for base, dirs, files in os.walk(abs_dir_name):
        cfg_file = os.path.join(base, 'config.json')
        if os.path.exists(cfg_file):
            file_paths.append(cfg_file)
    return file_paths 

if __name__ == '__main__':
    file_paths = retrieve_file_paths('./')
    print(file_paths)






import json 

def count_file(file):
    line_count = 0 
    non_empty_line_count = 0 
    token_count = 0 


    with open(file, 'r') as f:
        while True:
            #读取每行   
            line = f.readline()
            if not line:
                break 

            line_count += 1 
            line_len = len(line)
            line_token_count = 0 

            blank = False 
            for char in line:
                if char in ['', '\t', '\b']:
                    blank = True 
                else:
                    if blank: 
                        line_token_count += 1 
                        blank = False
            token_count += line_token_count 
            if line_token_count > 0:
                non_empty_line_count += 1

  
import os
import shutil
import logging 

logger = logging.getLogger(__name__)


def count_files_in_dir(dir):
    totalFiles = 0 
    for base, dirs, files in os.walk(dir):
        totalFiles += len(files)
    return totalFiles 

def zip_with_progress(dir_path, zip_file):
    bar = None 
    total_files = count_files_in_dir(fir_path)


    def progress(*args, **kwargs):
        if not args[0].startswith('adding'):
            return 

        nonlocal bar, total_files 
        if bar is None:
            print('@开始压缩:{}'.format(zip_file))
            bar = IncrementalBar('正在压缩：', max=total_files)
        bar.nex(1)

        old_info = logger.info 
        logger.info = lambda *args, **kwargs: progress(*args, **kwargs)
        shutil.make_archive(div_path, 'zip', dir_path, logger=logger)
        logger.info = old_info 

        if bar is not None:
            bar.finish()
if __name__ == '__main__':
    print()




from enum import Enum

class ErrorCode(Enum):
    SUCCESS = 0
    FAILED = 1
    NOT_FOUND = 2
    ALREADY_EXIST = 3
    INVALID_PARAMETERS = 4

    @staticmethod
    def internal_ret_2_http(ret):
        ret['err'] = ret['err'].name.lower()
      

if __name__ == '__main__':
    ret = {'err': ErrorCode.NOT_FOUND}
    ErrorCode.internal_ret_2_http(ret)
    assert ret['err'] == 'not_found'


import logging
from error_code import ErrorCode
from sqlite_connector import SqliteConnector
logger = logging.Logger(__name__)

class SqliteConnection(SqliteConnector):
    def __init__(self, db_file) -> None:
        super().__init__(db_file)

    def execute(self, sql, arg=None):
        

if __name__ == '__main__':
    kv = SqliteConnection("/tmp/test.db")

    ret = kv.open()
    assert ret['err'] == ErrorCode.SUCCESS

    sql = '''create table if not exists key_value (
        _key varchar(32) primary key not null,
        value text not null
    );'''
    ret = kv.execute(sql)
    assert ret['err'] == ErrorCode.SUCCESS
    ret = kv.close()
    assert ret['err'] == ErrorCode.SUCCESS






































































































