#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ldp'

try:
    # 已只读方式打开，第二个参数传 r；如果编码不对，会报 UnicodeDecodeError
    f = open('/Users/ldp/study/study-code/Python/fileio.py', 'r', encoding='utf-8')
    print(f.read())
finally:
    # 文件流需要在finally块中关闭
    if f:
        f.close()


# 可以用with语句来简化try finally
with open('/Users/ldp/study/study-code/Python/fileio.py', 'r', encoding='utf-8') as f:
    # 调用read()会一次性读取文件的全部内容
    # 保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
    # 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉


# 写文件时，如果需要覆盖原来的文件，则第二个参数传 w ；如果需要在原来的文件追加，则传入 a
# 写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
with open('/Users/ldp/test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, world!')
    f.write('中文')
