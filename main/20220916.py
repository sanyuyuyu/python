#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-16 18:47:08
# @Last Modified time: 2022-09-16 20:36:45
if __name__ == '__main__':
    unicode_str = u'er'
    print(unicode_str)

    utf8_str = unicode_str.encode('utf-8')
    print(utf8_str)

    unicode_str_again = utf8_str.decode('utf8')

    unicode_str_again = ...
   
import logging 
import json 


redis_connection_pool = None 

class RedisConnector():
    def __init__(self, host, port, password) -> None:
        global redis_connection_pool
        if redis_connection_pool is None:
            redis_connection_pool = redis.ConnectionPool(
                host=host,
                port=port,
                password=password
                )
        self.conn = None 

    def open(self):
        if self.conn is not None:
            return {"err": ErrorCode.SUCCESS}
        try: 
            self.cnn = redis.StrictRedis(
                connection_pool=redis_connection_pool)
            return {"err": ErrorCode.SUCCESS}
        except Exception as e: 
            logger.error('open redis exception:', str(e))
            self.conn = None 
            return {"err": ErrorCode.DB_OPEN_FAILED}

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None 
        return {"err": ErrorCode.SUCCESS}

if __name__ == '__main__':
    redis_connector = redisConnector("127.0.0.1", 6379, None)


    ret = redis_connector.open()
    assert ret['err'] == ErrorCode.SUCCESS
    ret = redis_connector.close()
    assert ret['err'] == ErrorCode.SUCCESS



import logging
import json
from error_code import ErrorCode
from redis_connector import RedisConnector
logger = logging.Logger(__name__)
redis_connection = None

class RedisKeyValueStore(RedisConnector):
    def __init__(self, host, port, password) -> None:
        super().__init__(host, port, password)

    def set(self, key, value):
        if self.coonn is None:
            return {'err': ErrorCode.DB_OPEN_FAILED}
        try: 
            self.conn.set(key, json.dumps(value))
            return {'err':ErrorCode.SUCCESS}
        except Exception as e:
            logger.error(f'set key:{key} exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}
    def get(self, key):
        if self.conn is None:
            return {'err': ErrorCode.DB_NOT_OPEN}

        try:
            results = self.conn.get(key)
            if results is None:
                return {"err": ErrorCode.NOT_FOUND}
            return {"err": ErrorCode.SUCCESS, "key": key, "value": json.loads(results)}
        except Exception as e:
            logger.error(f'get key:{key} exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}


if __name__ == '__main__':
    kv = RedisKeyValueStore("127.0.0.1", 6379, None)
    ret = kv.open()
    assert ret['err'] == ErrorCode.SUCCESS

    ret = kv.set("test", {"number": 0})
    assert ret['err'] == ErrorCode.SUCCESS

    ret = kv.get("test")
    assert ret['err'] == ErrorCode.SUCCESS
    assert ret['value']['number'] == 0

    ret = kv.close()
    assert ret['err'] == ErrorCode.SUCCESS
































