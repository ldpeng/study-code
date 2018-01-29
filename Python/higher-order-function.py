#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# map返回的是一个Iterator，是一个惰性序列，通过list函数把所有的值读出来
print(list(r))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 使用reduce对序列求和
from functools import reduce

def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

# 使用map和reduce将字符串转成int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('88965'));


# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


