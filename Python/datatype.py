#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 整数 ##
#Python对整数没有大小限制
#十六进制用0x前缀和0-9，a-f表示
a = 0xff00
b = 0xa5b4c3d2

## 浮点数 ##
#Python的浮点数没有大小限制，但是超出一定范围就直接表示为inf（无限大）
#对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代
c = 1.23e9
d = 1.2e-5

## 字符串 ##

#防止字符串中有较多转义字符，可用r''表示''内部的字符串默认不转义
print('\\\tabc\\')
print(r'\\\tabc\\')

#多行字符串使用'''...'''表示，无需较多的\n
print('''line1
line2
line3''')

#多行字符串也可以在前面加上r，表示不转译
print(r'''hello,\n
world''')

## 布尔类型 ##
#只有 True 和 False 两个值，注意大小写

#用 and、or和not 进行运算。
print(True and True);
print(True or False);
print(not 5 > 3);

## 空值 None ##
print(None)