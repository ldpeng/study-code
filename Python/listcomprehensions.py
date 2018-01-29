#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))


# 以下列表表达式可以生产 [1x1, 2x2, 3x3, ..., 10x10] 的 list
print([x * x for x in range(1, 11)]);

# 还可以添加 if 判断，只生产偶数的list
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

# 可同时迭代多个值
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

# 把 list 中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])