#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python 3版本中，字符串是以Unicode编码
# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(25991))

# 如果知道字符的整数编码，可以用十六进制表示字符串
print('\u4e2d\u6587')

# bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'

# Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# len()函数可以计算str包含多少个字符
print(len('ABC'))
print(len('中文'))

# 如果换成bytes，len()函数就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 在Python中，采用的格式化方式和C语言是一致的，用%实现
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# %s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))

# 字符串中需要用到%，则使用%%来表示一个%：
print('growth rate: %d %%' % 7)

# string是不可变对象
# 调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
a = 'abc'
print(a.replace('a', 'A'))
print(a)