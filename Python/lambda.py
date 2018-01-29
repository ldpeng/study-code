#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
