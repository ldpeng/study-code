#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在Python中，类似读写文件的必须使用try……finally保证资源释放的，可以通过with语句来简化。前提是实现了__enter__和__exit__这两个方法。
class Query(object):

    def __init__(self, name):
        self.name = name

    # 在with语句块前执行
    # def __enter__(self):
    #     print('Begin')
    #     return self

    # 在with语句块后执行
    # def __exit__(self, exc_type, exc_value, traceback):
    #     if exc_type:
    #         print('Error')
    #     else:
    #         print('End')

    def query(self):
        print('Query info about %s...' % self.name)

# with Query('Bob') as q:
#     q.query()

# 如果__enter__和__exit__仍然觉得繁琐，可以使用contextlib提供的@contextmanager这个decorator
# 这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
from contextlib import contextmanager

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

# 如果希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")


# 如果一个对象没有实现上下文，我们就不能把它用于with语句。
# 这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)

# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()