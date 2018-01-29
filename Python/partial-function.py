#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 通过设定参数的默认值，可以降低函数调用的难度。
# 如大量适用二进制字符串转数字
def int2(x, base=2):
    return int(x, base)

print(int2('1000000'))
print(int2('1010101'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))