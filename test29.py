#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-09-04 17:30:28
# @Last Modified time: 2022-09-04 19:31:25
class Pear():
    def name(self):
        print("pear pear")

    def func(self):
        print("yyyeah")


import types 
p = Pear()
print(dir(p))
print(type(p))


class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Point3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Vector3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

def test():
    points = [
        Point2D(0, 1),
        Point2D(0, 1),
        Point3D(0, 1, 2),
        Point3D(0, 1, 3),
        Vector2D(0, 1),
        Vector3D(0, 1, 4),
    ]

    z_objects = []
    for p in points:
        if hasattr(p, 'z'):
            z = getattr(p, 'z')
            print('get z attr', z)
            z_objects.append(p)
    
    for p in z_objects:
        print('x+y+z:', p.x+p.y+p.z)

if __name__ == '__main__':
    test()





































































