#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-07 12:17:03
import pymysql 
# SQL 插入语句
sql = """INSERT INTO BOOK(NAME,
         AUTHOR, PUBLISH, HAVE, HOT)
         VALUES ('001', 'test', '002', 100, 200)"""
# 查询
sql = "SELECT * FROM BOOK WHERE hot > 1000"

#修改
sql = "UPDATE BOOK SET name = 'ZS1000' WHERE hot > 1000"

#删除
sql = "delete FROM BOOK where  hot > 1000"

sql = """CREATE TABLE TEST (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
#删除表
sql = "DROP TABLE IF EXISTS TEST"



try:
    cur.execute(sql)
    db.commit()
except:
    print('have exception')
    db.rollback()

db.close()




import pymongo

mongo_client = pymongo.MongoClient("mongodb://192.168.1.200:30000")

print(mongo_client)

mongo_db = mongo_client["test"]

print(mongo_db)

#获取组合 
collist = mongo_db.list_collection_names()

#print(collist)

coll = mongo_db['new_coll']
#coll.insert_one({'name':'new_coll'})
#获取集合
#collist = mongo_db.list_collection_names()

coll = mongo_db["new_coll"]

for x in coll.find():
    print(x)


query_my = {"name":"new_coll"}
coll.delete_many(query_my


























































































































