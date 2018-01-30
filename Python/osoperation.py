#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ldp'

import os

# 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)

# 获取详细的系统信息。Windows不提供这方法
print(os.uname())

# 获取环境变量
print(os.environ)
print(os.environ.get('PATH'))

# 操作文件和目录

#查看当前目录
print(os.path.abspath('.'))
# 创建一个目录:
# os.mkdir('/Users/ldp/testdir')
# 删掉一个目录:
# os.rmdir('/Users/ldp/testdir')

# 不要直接拼接字符串路径，通过os.path.join()函数拼起来
s = os.path.join('/Users/michael', 'testdir')
print(s)

# 同样的，拆分目录通过os.path.split()
print(os.path.split(s))

# 截取文件扩展名
print(os.path.splitext('/Users/ldp/study/study-code/Python/osoperation.py'))

# 重命名当前目录下的文件
# os.rename('test.txt', 'test.py')

# os模块中没有复制文件的功能，原因是复制文件并非由操作系统提供的系统调用。
# 幸运的是shutil模块提供了copyfile()的函数
# shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# 列出当前目录下所有py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])