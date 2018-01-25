#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']

# 使用 len 函数，可以查看元素长度
print(len(classmates))

# 使用索引可以访问list元素，索引从0开始，超出范围会报 IndexError
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 索引可以从后面开始，如 -1 表示倒数第1个元素
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# 添加元素到尾部
classmates.append('Adam')
print(classmates)

# 根据索引插入指定位置
classmates.insert(1, 'Jack')
print(classmates)

# 删除指定索引元素，不传参数，则删除末尾元素
print(classmates.pop())
print(classmates)
print(classmates.pop(1))
print(classmates)

# 通过索引替换元素
classmates[1] = 'Sarah'
print(classmates)

# tuple 与 list 很类似，但tuple是不可变的，定时时必须赋值
# 由于 tuple 是不变的，所以可以作为键值来使用
# 要定义只有一个元素的 tuple 需要加个逗号，如t = (1,) 不然会认为是t = 1
t = (1, 2)