#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ldp'

import logging
# 有debug，info，warning，error等几个级别
logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        # 通过logging记录日志，可以输出到文件中
        logging.exception(e)
        # 抛异常
        raise e
    else:
        print('no error')
    finally:
        print('finally')

main()
print('END')

