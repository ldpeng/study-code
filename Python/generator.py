#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 要创建一个generator，第一种方法，只要把一个列表生成式的[]改成()
g = (x * x for x in range(10))
print(g);

# 通过next函数获取下一个值，如果没有下一个会报StopIteration。一般不这么做
# print(next(g))

# 通过for来遍历
for n in g:
    print(n)


# 第二种方法，通过 yield 关键字将函数返回值 return 替换掉
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print(f)

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable 但不是Iterator，不过可以通过iter()函数获得一个Iterator对象；
# for循环本质上就是通过不断调用next()函数；
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。




