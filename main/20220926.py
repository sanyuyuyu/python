# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-26 11:05:22

def check_param(key_value_map, key):
     assert key_value_map is not None
     assert type(key_value_map) == dict 
     assert key is not None 
     assert type(key) == str 


def get(key_value_map,key):
    check_param(key_value_map, key)
    return key_value_map.get(key)

def set(key_value_map,key,value):
    check_param(key_value_map, key)
    key_value_map[key] = value


if __name__ == '__main__':
    key_value_map = {}
    set(key_value_map, "test", {})
    value = get(key_value_map, "test")
    print("yes")
    assert type(value) == type({})
    assert value == {}






def check_param(key_value_map, key):
    assert key_value_map is not None and type(key_value_map) == type({})
    assert key is not None and type(key) == type("")
    

def get(key_value_map,key):
    check_param(key_value_map, key)
    return key_value_map.get(key)

def set(key_value_map,key,value):
    check_param(key_value_map, key)
    key_value_map[key] = value


if __name__ == '__main__':
    key_value_map = {}
    set(key_value_map, "test", {})
    value = get(key_value_map, "test")
    print( "so amazing")
    assert type(value) == type({})
    assert value == {}




def check_param(key_value_map, key):
    assert key_value_map is not None 
    assert type(key_value_map) == type({})
    assert key is not None 
    assert type(key) == type("")

   
def get(key_value_map,key):
    check_param(key_value_map, key)
    return key_value_map.get(key)

def set(key_value_map,key,value):
    check_param(key_value_map, key)
    key_value_map[key] = value


if __name__ == '__main__':
    key_value_map = {}
    set(key_value_map, "test", {})
    value = get(key_value_map, "test")
    print("wawgit ")
    assert type(value) == type({})
    assert value == {}






    



    