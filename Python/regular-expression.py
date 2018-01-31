#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ldp'

import re

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

# 常见方式：
# test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')

# 切分字符串

# 传统方式只能固定字符串切分
print('a b   c'.split(' '))
# 正则切分更灵活
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))


# 分组

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

# groups方法将所分组的字符串放在一个tuple中返回，不包括原字符串
print(m.groups())

# group(0)永远是原始字符串
print(m.group(0))
print(m.group(1))
print(m.group(2))


# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

print(re.match(r'^(\d+)(0*)$', '102300').groups())

# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 编译
# Python中使用正则表达式时，re模块内部会干两件事情：
#     编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
#     用编译后的正则表达式去匹配字符串。

# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())
