#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 和list比较，dict有以下几个特点：
#    查找和插入的速度极快，不会随着key的增加而变慢；
#    需要占用大量的内存，内存浪费多。
# 而list相反：
#    查找和插入的时间随着元素的增加而增加；
#    占用空间小，浪费内存很少。

# dict 的key值 和 set 只能放不可变对象，不然无法通过hash重新找到原来的值。试图使用可变对象插入，会报错。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d['Michael'])

# 过in判断key是否存在
print('Michael' in d)
print('Thomas' in d)

# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d.pop('Bob'))
print(d)


# 创建一个set，需要提供一个list作为输入集合：
s = set([1, 1, 2, 2, 3, 3])
print(s)

# add(key)方法可以添加元素到set中
s.add(4)
print(s)

# remove(key)方法可以删除元素：
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
