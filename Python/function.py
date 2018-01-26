#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数可以返回多个值，这些值组成一个tuple

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

print(x, y)

# 默认参数
# 第二个参数n的默认值设定为2，默认计算x的平方
# 默认参数要放在可变参数后面
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2))
print(power(2, 3))

### 默认参数不能用可变对象 ###
def add_end(L=[]):
    L.append('END')
    return L

### 此时，连续调用会有问题 ###
print(add_end())
print(add_end())
print(add_end())
### Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了 ###



# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2))

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
print(calc(*nums))


# 关键字参数 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

### **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。###
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数
# 例如，只接收city和job作为关键字参数。
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person1(name, age, *, city, job):
    print(name, age, city, job)

person1('Jack', 24, city='Beijing', job='Engineer')

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# print(person1('Jack', 24, 'Beijing', 'Engineer'))

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数可以有缺省值
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person3('Jack', 24, job='Engineer')


## 定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)

f2(1, 2, d=99, ext=None)


### 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的 ###
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args1 = (1, 2, 3)
kw1 = {'d': 88, 'x': '#'}
f2(*args1, **kw1)
