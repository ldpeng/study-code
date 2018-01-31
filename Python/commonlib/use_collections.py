#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('==============namedtuple=================')
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))


print('==============deque=================')
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


print('==============defaultdict=================')
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
# 创建时传入默认值
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值


print('==============OrderedDict=================')
# 如果要保持Key的顺序，可以用OrderedDict
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的


print('==============Counter=================')
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
