#!/usr/bin/env python3

from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        '''初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        '''
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        '''
        移动指定的增量
        :param dx: x轴的增量
        :param dy: y轴的增量
        '''
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        '''
        计算与另一个点的距离
        :param other: 另一个点
        '''
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '({},  {})'.format(self.x, self.y)

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()
