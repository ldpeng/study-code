#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

import functools

def log(func):
    # 为了保留原来的函数名，不需要编写wrapper.__name__ = func.__name__这样的代码
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 借助Python的@语法，把decorator置于函数的定义处：
# 相当于 now = log(now)
@log
def now():
    print('2015-3-25')

now()

print(now.__name__)

# 带参的情况 now = log('execute')(now)
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log1('execute')
def now1():
    print('2015-3-25')

now1()

print(now1.__name__)