# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-27 20:22:49

import json 


def load_json(file):
    with open(file, 'r') as f:
        return json.loads(f.read())

def dump_json(file, obj):
    with open(file, 'w') as f:
        f.write(json.dumps(obj, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    data = {
        'test': 1,
    }
    dump_json('test.json', data)
    load_json('test.json')