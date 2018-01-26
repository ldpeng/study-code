#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素
# L[0:3]表示，从索引0开始取，直到索引3为止，不包括索引3
print(L[0:3])
# 下面效果是等效的
print(L[:3])

# 切片也支持倒序索引
print(L[-2:])
print(L[-2:-1])

L = list(range(100))

print(L[:10])

# 前10个数，每两个取一个：
print(L[:10:2])
# 所有数，每5个取一个：
print(L[::5])

# 写[:]就可以原样复制一个list：
print(L[:])

# tuple 与 list 一样可以是用切片，string 也可以
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])