#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
# 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。因为针对相同的message，不同的key会产生不同的hash。

import hmac
message = b'Hello, world!'
key = b'secret'
# 注意：传入的key和message都是bytes类型
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

h = hmac.new(key, b'Hello', digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
h.update(b', ')
h.update(b'world')
h.update(b'!')
print(h.hexdigest())

