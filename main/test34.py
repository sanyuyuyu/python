#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-08 13:42:17
# @Last Modified time: 2022-09-08 20:30:21
import logging
import sqlite3 


class SqliteConnector():
    def __init__(self, db_file) -> None:
        self.db_file = db_file
        self.conn = None 

    def open(self):
        try:
            self.conn = sqlite3.connect(self.db_file, check_same_thread=True)
            return {"err": ErrorCode.SUCCESS}
        except Exception as e:
            logger.error('open sqlite exception:', str(e))
            self.close()
            return {"err":ErrorCode.DB_OPEN_FAILED}

    def close(self):
        if self.conn is not None:
            self.com.close()
            self.conn = None 
        return {'err':ErrorCode.SUCCESS}


if __name__ == '__main__':
    kv = SqliteConnector("/tmp/test.db")

    ret = kv.open()
    assert ret['err'] == ErrorCode.SUCCESS
    ret = kv.close()
    assert ret['err'] == ErrorCode.SUCCESS
















































