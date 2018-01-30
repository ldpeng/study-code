#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ldp'

# 有时候我们需要进行内存读写，可使用stringio 和bytesio

from io import StringIO
f = StringIO()

print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))

# getvalue()方法用于获得写入后的str。
print(f.getvalue())


f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


from io import BytesIO
f = BytesIO()
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。
f.write('中文'.encode('utf-8'))
print(f.getvalue())


f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())