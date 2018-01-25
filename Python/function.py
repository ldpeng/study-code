#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数可以返回多个值，这些值组成一个tuple

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

print(x, y)

# 默认参数
# 第二个参数n的默认值设定为2，默认计算x的平方
# 默认参数要放在可变参数后面
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2))
print(power(2, 3))

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2))

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
print(calc(*nums))