#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 协程

def consumer():
    r = ''
    while True:
        n = yield r
        # Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
        print(n)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    print('启动consumer generator')
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # 传递参数到generator中，并获取下一个值
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)