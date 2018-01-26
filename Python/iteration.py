#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 只要是可迭代对象，无论有无下标，都可以迭代
# 通过collections模块的Iterable类型 来判断对象是否可迭代
from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# for循环里，同时引用了两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# enumerate函数可以把一个list变成 索引-元素 对，这样就可以在for循环中同时迭代索引和元素本身：

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 迭代dict
d = {'a': 1, 'b': 2, 'c': 3}

# 迭代key
for key in d:
    print(key)
# 迭代value
for value in d.values():
    print(value)
# 同时迭代key和value
for k, v in d.items():
    print(k, v)