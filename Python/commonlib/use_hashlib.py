#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 摘要算法之所以能指出数据是否被篡改过
# 常见的摘要算法有MD5、SHA1

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md51 = hashlib.md5()
md51.update('how to use md5 in '.encode('utf-8'))
md51.update('python hashlib?'.encode('utf-8'))
print(md51.hexdigest())


# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())