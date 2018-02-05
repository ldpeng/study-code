#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# chardet可用于判断bytes的编码类型

import chardet

# detect方法返回一个dict，其中，encoding表示编码类型，confidence表示检测的概率1.0（即100%），language表示语言
print(chardet.detect(b'Hello, world!'))

# 检测GBK编码的中文：
print(chardet.detect('中文中文中文'.encode('gbk')))
# utf-8
print(chardet.detect('中文中文中文'.encode('utf-8')))

